# gif-weather
API that mashes up a weather service and a GIF service. This app is intended for use in examples and demos for my blog posts.

## Install Python Dependencies

```
pip install -r requirements.txt
```

## Run locally with uvicorn

Note: use `--reload` for development. It will automatically reload when the source is changed.

```
uvicorn main:app
uvicorn main:app --reload
```

## Build docker image

```
docker build . -t fullsnacktestengineer/gifweather:local
```

## Run docker container

```
docker run -p 8000:8000 fullsnacktestengineer/gifweather:local
```

## Run unit tests

```
pytest
```