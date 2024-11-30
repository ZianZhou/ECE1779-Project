# ECE1779-Project

# Website Performance Monitoring System

This project sets up a monitoring solution using a Python web server, Prometheus, and Grafana to monitor metrics such as request count, latency, and error rates. Alerts are configured for high latency and error rates, with data visualized on Grafana dashboards.

---

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Docker**: [Install Docker](https://www.docker.com/products/docker-desktop) and ensure Docker Engine is running.
2. **Prometheus**: [Install Prometheus](https://prometheus.io/download/) (v2.37.0 or higher).
3. **Grafana**: [Install Grafana](https://grafana.com/grafana/download/) (v9.2.0 or higher).

---

## Running the Project

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/website-monitoring.git
cd web_server
```

### Step 2: Start the container

```bash
docker-compose up --build
curl http://localhost:5000/simulate_error
```

### Step 3: Clean up

```bash
docker-compose down
docker-compose down -v
```
