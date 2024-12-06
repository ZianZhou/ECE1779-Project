from locust import HttpUser, task, between, constant_throughput
import random

class WebMonitoringTest(HttpUser):
    # Define user behavior and wait time
    wait_time = between(1, 3)  # Adjust for realistic load simulation
    
    @task(5)
    def simulate_user_behavior(self):
        """Simulate various user behaviors across endpoints."""
        endpoints = ["/", "/metrics", "/nonexistent"]
        endpoint = random.choice(endpoints)
        with self.client.get(endpoint, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                print(f"User Behavior: Accessed {endpoint} successfully")
            elif response.status_code == 404:
                response.failure(f"{endpoint} not found")
            else:
                response.failure(f"Unexpected status {response.status_code} for {endpoint}")

    @task(4)
    def test_latency(self):
        """Test HTTP request latency for the homepage."""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                print(f"Latency Test: Response time = {response.elapsed.total_seconds()} seconds")
            else:
                response.failure(f"Failed with status code {response.status_code}")

    @task(3)
    def simulate_concurrent_users_root(self):
        """Simulate load on the / endpoint."""
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                print(f"/ throughput: Successful response in {response.elapsed.total_seconds()} seconds")
            else:
                response.failure(f"Failed to fetch metrics: {response.status_code}")

    @task(2)
    def simulate_concurrent_users_metrics(self):
        """Simulate load on the /metrics endpoint."""
        with self.client.get("/metrics", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                print(f"/metrics throughput: Successful response in {response.elapsed.total_seconds()} seconds")
            else:
                response.failure(f"Failed to fetch metrics: {response.status_code}")

    @task(1)
    def stress_test(self):
        """Simulate stress testing by hitting the same endpoint repeatedly."""
        # Reduce the wait time for stress testing
        self.client.get("/metrics", timeout=1)  # Simulate a heavy load scenario
