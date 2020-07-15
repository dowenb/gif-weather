from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"endpoints": ["/locations", "/weather/<location_name>", "/gif/<weather>"]}

def test_locations():
    response = client.get("/locations")
    assert response.status_code == 200
    assert response.json() == {"locations": ["London", "Nottingham", "Sheffield"]}

def test_weather_location_london():
    response = client.get("/weather/london")
    assert response.status_code == 200
    assert response.json() == {"wether": "raining"}

def test_weather_location_not_found():
    response = client.get("/weather/invalid")
    assert response.status_code == 404
    assert response.json() == {"detail": "Location not found. GET /locations for an acceptable list."}

def test_gif_for_weather_sunny():
    response = client.get("/gif/sunny")
    assert response.status_code == 200
    assert response.json() == {"url": "https://giphy.com/gifs/worldweatherru-weather-in-las-vegas-on-the-map-h6rZJnvF2fktJ8f7Oc"}

def test_gif_for_weather_not_found():
    response = client.get("/gif/invalid")
    assert response.status_code == 404
    assert response.json() == {"detail": "GIF not found."}