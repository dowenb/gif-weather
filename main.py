from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"endpoints": ["/locations", "/weather/<location_name>", "/gif/<weather>"]}


@app.get("/locations")
async def locations():
    return {"locations": ["London", "Nottingham", "Sheffield"]}


@app.get("/weather/{location_name}")
async def weather_at_location(location_name):
    # TODO: Replace static returns with an integration with a weather service
    if location_name.lower() == "london":
        return {"wether": "raining"}
    elif location_name.lower() == "nottingham":
        return {"weather": "sunny"}
    elif location_name.lower() == "sheffield":
        return {"weather": "windy"}
    else:
        raise HTTPException(
            status_code=404, detail="Location not found. GET /locations for an acceptable list.")


@app.get("/gif/{weather}")
async def gif_for_weather(weather):
    # TODO: Replace static returns with an integration with Giphy
    if weather.lower() == "raining":
        return {"url": "https://giphy.com/gifs/dog-rain-storm-xUPGciUP5rUdUEeOg8"}
    elif weather.lower() == "sunny":
        return {"url": "https://giphy.com/gifs/worldweatherru-weather-in-las-vegas-on-the-map-h6rZJnvF2fktJ8f7Oc"}
    elif weather.lower() == "windy":
        return {"url": "https://giphy.com/gifs/go-plane-M9tpu3TPG42n6"}
    else:
        raise HTTPException(
            status_code=404, detail="GIF not found.")
