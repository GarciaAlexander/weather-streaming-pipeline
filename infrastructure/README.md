# Infrastructure Overview

This folder contains the Docker-based infrastructure required to run the Weather Streaming Pipeline. It provides local instances of Kafka, Zookeeper, and Schema Registry so the producer and consumer can operate exactly as they would in a real streaming environment.

---

## Components

Zookeeper  
Coordinates Kafka’s internal metadata and broker management.

Kafka  
Message broker responsible for receiving weather events from the producer and delivering them to the consumer.  
Two listeners are configured:

- Internal listener for communication between Docker containers.
- External listener so Python applications on the host machine can connect.

Schema Registry  
Stores and manages Avro schemas.  
Ensures the producer and consumer use compatible schema versions.

---

## Docker Compose Services

The `docker-compose.yml` file defines three services:

- zookeeper
- kafka
- schema-registry

Each service includes the necessary ports, environment variables, and networking configuration for local development.

---

## Ports

Zookeeper: 2181  
Kafka internal: 9092  
Kafka external: 29092  
Schema Registry: 8081

The external Kafka listener (29092) is required for host-based Python clients.

---

## Starting the Infrastructure

Run this command inside the `infrastructure` folder:

    docker-compose up -d

This starts all services in detached mode.

---

## Stopping the Infrastructure

    docker-compose down

This stops and removes all containers.

---

## Verifying Kafka

Check running containers:

    docker ps

You should see:

- kafka
- zookeeper
- schema-registry

---

## Verifying Schema Registry

Open this URL in a browser:

http://localhost:8081/subjects

Before running the producer, it will show:

[]

After running the producer, it will show:

["weather_event"]

---

## Notes

This setup is intended for local development.  
Dual listeners allow both Docker containers and host applications to communicate with Kafka.  
Schema Registry ensures consistent Avro schema usage across the pipeline.  
This infrastructure provides a reliable foundation for real-time streaming workloads and can be extended for cloud deployment.
