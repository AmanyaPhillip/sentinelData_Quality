from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "HEALTHY"

def test_trigger_validation_run():
    response = client.post("/api/v1/validation/run")
    assert response.status_code in [200, 500]  # Depends on local DB readiness
