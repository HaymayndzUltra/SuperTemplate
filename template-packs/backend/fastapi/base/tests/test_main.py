"""
Test main endpoints
"""
from fastapi.testclient import TestClient

from app.config import settings


def test_read_root(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == f"{settings.PROJECT_NAME} API"
    assert "version" in data