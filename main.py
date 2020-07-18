from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{location}")
async def gif_weather(location):
    weather = weather_at_location(location)
    gif = gif_for_weather(weather)
    return gif


def weather_at_location(location_name):
    # Get the "Where in the world ID" for the location name
    request_url = 'https://www.metaweather.com/api/location/search/?query={location}'.format(
        location=location_name)
    response = requests.get(request_url)
    response_json = response.json()
    if response_json == []:
        raise HTTPException(status_code=404, detail="Weather location not found.")
    else:    
        woeid = response_json[0]["woeid"]
        # Get the weather description
        request_url = 'https://www.metaweather.com/api/location/{woeid}/'.format(
            woeid=woeid)

    response = requests.get(request_url)
    if response.ok:
        response_json = response.json()
        location_weather = response_json["consolidated_weather"][0]["weather_state_name"]
        return {"weather": location_weather}
    else:
        raise HTTPException(
            status_code=404, detail="Weather not found.")


def gif_for_weather(weather):
    request_url = 'https://api.giphy.com/v1/gifs/search?api_key=dc6zaTOxFJmzC&q={weather}&limit=1&offset=0&rating=g&lang=en'.format(
        weather=weather)
    response = requests.get(request_url)
    if response.ok:
        response_json = response.json()
        return response_json
    else:
        raise HTTPException(
            status_code=404, detail="GIF not found.")
