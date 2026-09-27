# Producer Service

---

## Overview

The producer service retrieves weather data from the OpenWeather API, converts it into an Avro record, and sends it to Kafka. It is responsible for data ingestion and schema‑validated message production.

---

## Responsibilities

- Call the OpenWeather API for current weather data.
- Extract required fields (city, timestamp, temperature, humidity, wind speed, conditions).
- Serialize the data using the Avro schema stored in the schemas folder.
- Register and validate the schema using Schema Registry.
- Send Avro‑encoded messages to Kafka on the `weather-events` topic.
- Implement retry logic for API failures and Kafka delivery issues.
- Log all activity using the shared logger module.

---

## File Structure

- `producer.py` — main producer script
- `requirements.txt` — Python dependencies for the producer

---

## How to Run

Activate your virtual environment, then run:

    python -m producer.producer

The producer will begin sending weather events to Kafka.

---

## Dependencies

Dependencies are listed in `producer/requirements.txt` and include:

- Kafka client
- Avro serializer
- HTTP client for API calls

---

## Notes

- The producer automatically registers the Avro schema if it does not exist.
- If Kafka or Schema Registry is unavailable, the producer retries until services are ready.
- Logs are generated using the shared logger module in the `common` folder.
