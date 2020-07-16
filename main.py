from fastapi import FastAPI, HTTPException
import requests
app = FastAPI()


@app.get("/")
async def root():
    return {"endpoints": ["/locations", "/weather/<location_name>", "/gif/<weather>"]}


@app.get("/locations")
async def locations():
    return {"locations": ["London", "Nottingham", "Sheffield"]}


@app.get("/weather/{location_name}")
async def weather_at_location(location_name):
    # Get the "Where in the world ID" for the location name
    request_url = 'https://www.metaweather.com/api/location/search/?query={location}'.format(location=location_name)
    response = requests.get(request_url)
    response_json = response.json()
    woeid = response_json[0]["woeid"]
    # Get the weather description
    request_url = 'https://www.metaweather.com/api/location/{woeid}/'.format(woeid=woeid)
    response = requests.get(request_url)
    response_json = response.json()
    location_weather = response_json["consolidated_weather"][0]["weather_state_name"]

    if response.ok:
        return {"weather": location_weather}
    else:
        raise HTTPException(
            status_code=404, detail="Weather not found.")


@app.get("/gif/{weather}")
async def gif_for_weather(weather):
    request_url = 'https://api.giphy.com/v1/gifs/search?api_key=QloqXubxa4z9GgZQ6JqwbAeXbscVzz97&q={weather}&limit=1&offset=0&rating=g&lang=en'.format(
        weather=weather)
    response = requests.get(request_url)
    response_json = response.json()
    gif_url = response_json["data"][0]["url"]

    if response.ok:
        return {"url": gif_url}
    else:
        raise HTTPException(
            status_code=404, detail="GIF not found.")
