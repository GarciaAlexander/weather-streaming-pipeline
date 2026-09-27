# Avro Schemas

---

## Overview

This folder contains the Avro schema used by both the producer and consumer. The schema defines the structure of each weather event sent through Kafka and ensures consistent, validated communication across the streaming pipeline.

---

## Purpose

- Provide a strict, versioned data structure for weather events.
- Ensure compatibility between producer and consumer.
- Enable Schema Registry to validate and manage schema versions.
- Prevent malformed or incompatible messages from entering the pipeline.

---

## Schema File

`weather_event.avsc`

This file defines the Avro record used throughout the system.

Fields included:

- city (string)
- timestamp (string)
- temperature (float)
- humidity (int)
- wind_speed (float)
- conditions (string)

These fields represent the core weather attributes retrieved from the OpenWeather API.

---

## How It Is Used

### Producer

- Loads the schema from this folder.
- Serializes weather events into Avro format.
- Registers the schema with Schema Registry if not already present.

### Consumer

- Retrieves the schema from Schema Registry.
- Deserializes incoming Avro messages.
- Converts the record into JSON before uploading to S3.

---

## Schema Registry Integration

The schema is automatically registered with Schema Registry the first time the producer sends a message.  
Schema Registry ensures:

- Version control
- Compatibility checks
- Safe schema evolution

If the schema changes, a new version will be created automatically.

---

## Notes

- Both producer and consumer must remain compatible with the schema.
- Any schema changes should be carefully planned to avoid breaking downstream systems.
- This folder should contain all Avro schemas used in the pipeline.
