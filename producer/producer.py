from common.logger import logger
import time
import requests
from datetime import datetime

from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

from common.config import (
    BOOTSTRAP_SERVERS,
    TOPIC_NAME,
    API_URL,
    CITY,
    SCHEMA_REGISTRY_URL,
)

MAX_RETRIES = 3


# -----------------------------
# Weather API with retry logic
# -----------------------------
def fetch_weather():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(API_URL, timeout=5)
            response.raise_for_status()
            data = response.json()

            return {
                "city": CITY,
                "timestamp": datetime.utcnow().isoformat(),
                "temperature": float(data["main"]["temp"]),
                "humidity": int(data["main"]["humidity"]),
                "wind_speed": float(data["wind"]["speed"]),
                "conditions": data["weather"][0]["description"],
            }

        except Exception as e:
            logger.error(f"API error (attempt {attempt}): {e}")
            time.sleep(1)

    logger.error("API permanently failed after retries.")
    return None


# -----------------------------
# Kafka produce with retry logic
# -----------------------------
def safe_produce(producer, topic, value):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            producer.produce(topic=topic, value=value)
            logger.info(f"Produced message: {value}")
            return
        except Exception as e:
            logger.error(f"Produce failed (attempt {attempt}): {e}")
            time.sleep(1)

    logger.error("Message permanently failed after retries.")


# -----------------------------
# Schema Registry + Avro setup
# -----------------------------
schema_registry = SchemaRegistryClient({"url": SCHEMA_REGISTRY_URL})

with open("schemas/weather_event.avsc", "r") as f:
    avro_schema_str = f.read()

avro_serializer = AvroSerializer(schema_registry, avro_schema_str)

producer = SerializingProducer(
    {"bootstrap.servers": BOOTSTRAP_SERVERS, "value.serializer": avro_serializer}
)


# -----------------------------
# Main loop
# -----------------------------
if __name__ == "__main__":
    logger.info(f"Producer started. Using Kafka at {BOOTSTRAP_SERVERS}")

    while True:
        weather_event = fetch_weather()

        if not weather_event:
            logger.error("Skipping event due to API failure.")
            continue

        safe_produce(producer, TOPIC_NAME, weather_event)

        try:
            producer.flush()
        except Exception as e:
            logger.error(f"Flush failed: {e}")

        time.sleep(10)
