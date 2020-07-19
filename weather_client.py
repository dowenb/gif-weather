"""Client for getting the current weather at a location."""

from fastapi import HTTPException
import requests


def weather_at_location(location_name):
    """Returns a JSON object that describe the current weather for the chosen location.
    Uses infomation from the metaweather API.
    """
    # Get the "Where in the world ID" for the location name
    request_url = ('https://www.metaweather.com/api/location/search/?'
                   'query={location}'.format(
                       location=location_name))
    
    response = requests.get(request_url)
    response_json = response.json()
    
    if response_json == []:
        raise HTTPException(
            status_code=404, detail="Weather location not found.")

    woeid = response_json[0]["woeid"]
    # Get the weather description
    request_url = 'https://www.metaweather.com/api/location/{woeid}/'.format(
        woeid=woeid)

    response = requests.get(request_url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=404, detail="Weather not found.")

    response_json = response.json()
    location_weather = response_json["consolidated_weather"][0]["weather_state_name"]
    return {"weather": location_weather}
