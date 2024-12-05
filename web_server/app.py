from flask import Flask, request, jsonify
import time
import random
from metrics import setup_metrics

app = Flask(__name__)

# Simulate metrics
metrics = {
    "request_count": 0,
    "error_count": 0,
    "latency_sum": 0,
}

setup_metrics(app)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_metrics(response):
    # Calculate latency
    latency = time.time() - request.start_time
    metrics["request_count"] += 1
    metrics["latency_sum"] += latency

    # Log errors
    if response.status_code >= 400:
        metrics["error_count"] += 1

    return response

@app.route("/", methods=["GET"])
def home():
    time.sleep(random.uniform(0.1, 0.3))  # Simulate processing time
    return "Welcome to the Python Web Server!"

@app.route("/metrics", methods=["GET"])
def metrics_endpoint():
    # Expose metrics in a Prometheus-compatible format
    response = (
        f"# HELP http_requests_total The total number of HTTP requests.\n"
        f"# TYPE http_requests_total counter\n"
        f"http_requests_total {metrics['request_count']}\n"
        
        f"# HELP http_errors_total The total number of HTTP errors.\n"
        f"# TYPE http_errors_total counter\n"
        f"http_errors_total {metrics['error_count']}\n"
        
        f"# HELP http_request_latency_seconds_total The total latency in seconds.\n"
        f"# TYPE http_request_latency_seconds_total counter\n"
        f"http_request_latency_seconds_total {metrics['latency_sum']:.4f}\n"
    )
    return response, 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.route("/simulate_error", methods=["GET"])
def simulate_error():
    time.sleep(random.uniform(0.1, 0.3))  # Simulate processing time
    return jsonify({"error": "This is a simulated error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
