from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_gif_weather():
    response = client.get("/london")
    assert response.status_code == 200