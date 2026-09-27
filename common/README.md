# Common Utilities

---

## Overview

The `common` folder contains shared modules used by both the producer and consumer services. These modules provide centralized configuration management and standardized logging, ensuring consistency across the entire streaming pipeline.

---

## Purpose

- Avoid duplicated configuration code across services.
- Provide a unified logging format for debugging and monitoring.
- Centralize shared utilities for maintainability and clarity.
- Ensure both producer and consumer operate with consistent settings.

---

## Files

### config.py

Handles shared configuration values such as:

- API keys
- Kafka connection settings
- Schema Registry URLs
- S3 bucket names
- Environment variables

This module ensures both producer and consumer use the same configuration source.

### logger.py

Provides a standardized logging setup:

- Timestamped log entries
- Consistent formatting
- Shared logger instance
- Support for both producer and consumer

This module helps with debugging, monitoring, and error tracking across the pipeline.

---

## How It Is Used

### Producer

- Imports `config.py` for API keys, Kafka URLs, and Schema Registry settings.
- Uses `logger.py` to log API calls, Kafka delivery attempts, retries, and errors.

### Consumer

- Imports `config.py` for Kafka URLs, Schema Registry settings, and S3 bucket configuration.
- Uses `logger.py` to log Kafka polling, deserialization events, S3 uploads, and errors.

---

## Notes

- Any new shared functionality should be added to this folder.
- Keeping shared utilities centralized improves maintainability and reduces duplication.
- Both services rely on these modules for consistent behavior and logging.
