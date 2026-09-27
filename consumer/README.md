# Consumer Service

---

## Overview

The consumer service reads Avro‑encoded weather events from Kafka, deserializes them using Schema Registry, and stores each event in Amazon S3. It is responsible for downstream processing and cloud storage integration.

---

## Responsibilities

- Connect to Kafka using the external listener (29092).
- Poll the `weather-events` topic for new messages.
- Deserialize Avro records using the schema stored in Schema Registry.
- Convert each record into a JSON object.
- Upload the JSON file to S3 in a structured folder format.
- Implement retry logic for Kafka polling and S3 upload failures.
- Log all activity using the shared logger module.

---

## File Structure

- `consumer.py` — main consumer script
- `requirements.txt` — Python dependencies for the consumer

---

## How to Run

Activate your virtual environment, then run:

    python -m consumer.consumer

The consumer will begin reading messages from Kafka and uploading them to S3.

---

## S3 Folder Structure

Events are stored in the following format:

    s3://<your-bucket>/weather-events/<city>/<timestamp>.json

This structure allows easy querying, partitioning, and downstream analytics.

---

## Dependencies

Dependencies are listed in `consumer/requirements.txt` and include:

- Kafka client
- Avro deserializer
- AWS SDK (boto3)

---

## Notes

- The consumer requires valid AWS credentials to upload to S3.
- If Kafka or Schema Registry is unavailable, the consumer retries until services are ready.
- Logs are generated using the shared logger module in the `common` folder.
