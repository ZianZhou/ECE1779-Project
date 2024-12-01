import requests

def test_homepage():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert "Welcome" in response.text

def test_metrics_endpoint():
    response = requests.get("http://localhost:5000/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text

if __name__ == "__main__":
    test_homepage()
    test_metrics_endpoint()
    print("All tests passed.")
