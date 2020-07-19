"""GIF Weather API """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from weather_client import weather_at_location
from gif_client import gif_for_weather

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
    """
    Return a JSON response for a GIF that represents,
    the current weather at the requested Location.
    """
    weather = weather_at_location(location)
    gif = gif_for_weather(weather)
    return gif
