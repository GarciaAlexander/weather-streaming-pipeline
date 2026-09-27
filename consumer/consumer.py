from common.logger import logger
import json
import boto3
import time

from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

from common.config import (
    BOOTSTRAP_SERVERS,
    TOPIC_NAME,
    AWS_BUCKET_NAME,
    SCHEMA_REGISTRY_URL,
)

# -----------------------------
# S3 client
# -----------------------------
s3 = boto3.client("s3")

# -----------------------------
# Schema Registry + Avro setup
# -----------------------------
schema_registry = SchemaRegistryClient({"url": SCHEMA_REGISTRY_URL})

with open("schemas/weather_event.avsc", "r") as f:
    avro_schema_str = f.read()

avro_deserializer = AvroDeserializer(schema_registry, avro_schema_str)

# -----------------------------
# Kafka Consumer config
# -----------------------------
consumer_conf = {
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "key.deserializer": None,
    "value.deserializer": avro_deserializer,
    "group.id": "weather-consumer-group",
    "auto.offset.reset": "earliest",
}

consumer = DeserializingConsumer(consumer_conf)
consumer.subscribe([TOPIC_NAME])

logger.info(f"Consumer started. Listening on topic '{TOPIC_NAME}'")


# -----------------------------
# S3 upload with error handling
# -----------------------------
def upload_to_s3(event):
    try:
        timestamp = event["timestamp"].replace(":", "-")
        key = f"weather-events/{event['city']}/{timestamp}.json"

        s3.put_object(Bucket=AWS_BUCKET_NAME, Key=key, Body=json.dumps(event))

        logger.info(f"Uploaded to S3: {key}")

    except Exception as e:
        logger.error(f"S3 upload failed: {e}")


# -----------------------------
# Main loop
# -----------------------------
try:
    while True:
        try:
            msg = consumer.poll(1.0)
        except Exception as e:
            logger.error(f"Poll error: {e}")
            continue

        if msg is None:
            continue

        if msg.error():
            logger.error(f"Kafka message error: {msg.error()}")
            continue

        try:
            event = msg.value()
            logger.info(f"Received (Avro): {event}")
        except Exception as e:
            logger.error(f"Deserialization failed: {e}")
            continue

        upload_to_s3(event)

except KeyboardInterrupt:
    logger.info("Consumer shutting down gracefully...")

finally:
    consumer.close()
