![Python](https://img.shields.io/badge/Python-3.11-blue)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Avro](https://img.shields.io/badge/Avro-Schema-orange)
![AWS S3](https://img.shields.io/badge/AWS-S3-yellow)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

# Weather Streaming Pipeline — Kafka + Avro + Schema Registry + S3

A production‑grade real‑time data pipeline that streams weather data from the OpenWeather API into Kafka, validates messages using Avro + Schema Registry, and stores events in Amazon S3 for downstream analytics.

This project demonstrates real engineering skills:

- Real‑time ingestion
- Schema‑validated streaming
- Cloud storage integration
- Production‑grade logging
- Retry logic + error handling
- Clean architecture
- Professional documentation

---

## 📌 Architecture Overview

OpenWeather API to Producer (Python) to Kafka to Schema Registry to Consumer (Python) to S3

### Components

- Kafka Broker (Docker)
- Schema Registry (Docker)
- Python Producer (Avro serialization)
- Python Consumer (Avro deserialization)
- Amazon S3 Storage
- Centralized Logging System
- Retry Logic for API, Kafka, and S3

---

## Project Structure

```
weather-streaming-pipeline/
│
├── infrastructure/
│   ├── docker-compose.yml
│   └── README.md
│
├── producer/
│   ├── producer.py
│   └── requirements.txt
│   └── README.md
│
├── consumer/
│   ├── consumer.py
│   └── requirements.txt
│   └── README.md
│
├── common/
│   ├── config.py
│   ├── logger.py
│   └── README.md
│
├── schemas/
│   └── weather_event.avsc
│   └── README.md
│
└── README.md
```

---

## 🗓️ 7‑Day Build Plan (Completed)

### Day 1 — Kafka Setup

- Docker Compose for Kafka + Schema Registry
- Dual listeners (9092 internal, 29092 external)

### Day 2 — Python Producer

- Basic producer sending JSON
- Verified Kafka connectivity

### Day 3 — Python Consumer

- Consumed messages
- Uploaded events to S3

### Day 4 — API Integration

- Connected producer to OpenWeather API
- Real weather data flowing into Kafka

### Day 5 — Schema Registry + Avro

- Added Avro schema
- Producer serializes Avro
- Consumer deserializes Avro
- Full schema validation

### Day 6 — Error Handling + Logging

- Retry logic for API, Kafka, and S3
- Structured logging
- Graceful shutdown
- Production‑grade pipeline

### Day 7 — Documentation

- Created professional README
- Prepared repo for GitHub
- Ready for portfolio + interviews

---

## 🧩 Avro Schema

schemas/weather_event.avsc

{
"type": "record",
"name": "WeatherEvent",
"namespace": "com.weather",
"fields": [
{"name": "city", "type": "string"},
{"name": "timestamp", "type": "string"},
{"name": "temperature", "type": "float"},
{"name": "humidity", "type": "int"},
{"name": "wind_speed", "type": "float"},
{"name": "conditions", "type": "string"}
]
}

---

## 🚀 Producer (Python)

### Responsibilities:

- Fetch weather data from API
- Validate + serialize using Avro
- Send to Kafka
- Retry on failure
- Log all events

### Key Features:

- API retry logic
- Kafka retry logic
- Structured logging
- Avro serialization
- Schema Registry integration

---

## 📥 Consumer (Python)

### Responsibilities:

- Poll Kafka
- Deserialize Avro
- Upload events to S3
- Handle deserialization errors
- Handle S3 upload failures
- Log all events

### Key Features:

- Avro deserialization
- S3 upload with error handling
- Structured logging
- Graceful shutdown

---

## ☁️ S3 Folder Structure

s3://kafka-stream-events/weather-events/Orlando/2026-09-23T15-27-35.json

Each file contains one Avro‑validated weather event.

---

## 🧪 How to Run Locally

### 1. Start Kafka

    cd infrastructure
    docker-compose up -d

### 2. Activate virtual environment

    source venv/Scripts/activate

### 3. Start Consumer

    python -m consumer.consumer

### 4. Start Producer

    python -m producer.producer

---

## 📊 What You Can Build Next

- Athena + Glue table over S3
- QuickSight dashboard
- Airflow DAG for daily aggregation
- Multi‑topic streaming (alerts, traffic, air quality)
- Schema evolution (add new fields safely)
- Deploy producer/consumer to AWS ECS or Lambda

---

## 🎯 Skills Demonstrated

- Kafka architecture
- Schema Registry + Avro
- Real‑time API ingestion
- Cloud storage integration
- Error handling + retries
- Logging best practices
- Docker networking
- Production‑grade Python pipeline
- End‑to‑end documentation

---

## 🏁 Final Notes

This pipeline follows modern data engineering standards for real‑time ingestion, schema‑validated streaming, and cloud‑based storage. The project is structured for clarity, maintainability, and extensibility, making it suitable for production environments or integration into larger data platforms.

The implementation demonstrates:

- Reliable ingestion of external API data
- Strong schema governance using Avro + Schema Registry
- Fault‑tolerant processing with retries and structured logging
- Cloud‑ready storage patterns using Amazon S3
- Clean separation of concerns across infrastructure, ingestion, processing, and configuration

This repository can serve as a foundation for additional streaming workloads, downstream analytics, or orchestration via Airflow, Glue, or other enterprise tools.
