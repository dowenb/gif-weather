"""Client for getting a GIF based on keyword. """

from fastapi import HTTPException
import requests


def gif_for_weather(search_word, limit=1):
    """Return a JSON response for the first GIF
    from Giphy Search based on the search word provided.
    """
    request_url = ('https://api.giphy.com/v1/gifs/search?'
                   'api_key=dc6zaTOxFJmzC'
                   '&q={search_word}'
                   '&limit={limit}&offset=0&rating=g&lang=en'.format(
                       search_word=search_word, limit=limit))

    response = requests.get(request_url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=404, detail="GIF not found.")

    response_json = response.json()
    return response_json
