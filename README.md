# ECE1779-Project

# Website Performance Monitoring System

This project sets up a monitoring solution using a Python web server, Prometheus, and Grafana to monitor metrics such as request count, latency, and error rates. Alerts are configured for high latency and error rates, with data visualized on Grafana dashboards.

## Features

- Real-time request monitoring
- Response time tracking and latency analysis
- Error rate monitoring
- System resource monitoring (CPU, Memory)
- Custom alerts for performance issues
- Interactive Grafana dashboards

## Available Metrics

- Request Rate (requests per second)
- Error Rate
- Response Time Distribution
- Memory Usage
- CPU Usage
- Request Duration Distribution (Latency Heatmap)

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Docker**: [Install Docker](https://www.docker.com/products/docker-desktop) and ensure Docker Engine is running.
2. **Prometheus**: [Install Prometheus](https://prometheus.io/download/) (v2.37.0 or higher).
3. **Grafana**: [Install Grafana](https://grafana.com/grafana/download/) (v9.2.0 or higher).

## Running the Project

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/website-monitoring.git
cd ECE1779-Project
```

### Step 2: Start the container

```bash
docker-compose up --build
```

### Step 3: Access the Services

- Web Server: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (login: admin/admin)

  View Metrics:

  - Request rate
  - Error rate
  - Response time
  - System resources

  Note: If you don't see data immediately, try generating some test traffic using the curl commands in Step 4.

### Step 4: Test the monitoring

```bash
# Generate some test traffic
curl http://localhost:5000/
curl http://localhost:5000/simulate_error
```

### Step 5: Clean up

```bash
docker-compose down
docker-compose down -v
```

# Pulling the docker image from docker hub

This repository hosts a containerized solution for monitoring website performance using a Dockerized web server. The system collects metrics and provides observability through Prometheus and Grafana.

## Docker Image

The Docker image for this project is hosted on Docker Hub. You can pull and run the image to set up the web server locally or integrate it into your infrastructure.

---

## How to Use the Docker Image

### Step 1: Pull the Docker Image

To pull the image from Docker Hub, use the following command:

```bash
docker pull zanyguy/web-monitoring:latest:latest

docker run -p 5000:5000 zanyguy/web-monitoring:latest:latest

docker run -p 5000:5000 -e CUSTOM_ENV_VAR=value zanyguy/web-monitoring:latest:latest

docker pull zanyguy/web-monitoring:latest:latest
docker run -p 5000:5000 zanyguy/web-monitoring:latest:latest
curl http://localhost:5000/metrics
docker ps
docker stop <container-id>
docker rm <container-id>

```
---
# Testing
This project contains a Locust-based testing script to evaluate the performance of a web monitoring system. The tests are designed to measure HTTP request latency, throughput, error rates, and simulate different user behaviors for key endpoints.

## Features
- HTTP Request Latency: Measure the time it takes to receive responses from the server.
- Throughput Testing: Evaluate the number of requests the server can handle per second.
- Error Rate Monitoring: Identify and log failure rate during testing.
- Endpoint-Specific Metrics: Simulate different user behaviors across key endpoints (/, /metrics, /nonexistent).
- Load Testing: Simulate multiple concurrent users accessing the system.
- Stress Testing: Push the system to its limits to identify breaking points.

## Usage
### Step 1
Install Locust globally or in a virtual environment： 
```bash
pip install locust
```
### Step 2
Execute the Locust command:
```bash
locust -f tests/locustfile.py
```

### Step 3
By default, Locust will start a web interface at http://localhost:8089. Access it via your browser.
Set the number of users, spawn rate and host.

