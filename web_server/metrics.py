from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from flask import Response, g
import time

# Define monitoring metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

def setup_metrics(app):
    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    # Request count middleware
    @app.before_request
    def before_request():
        REQUEST_COUNT.inc()

    # Request latency middleware
    @app.before_request
    def start_timer():
        g.start = time.time()

    @app.after_request
    def record_request_time(response):
        if hasattr(g, 'start'):
            resp_time = time.time() - g.start
            REQUEST_LATENCY.observe(resp_time)
        return response