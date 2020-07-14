# gif-weather
API that mashes up a weather service and a GIF service. This app is intended for use in examples and demos for my blog posts.

## Install Python Dependencies

```
pip install -r requirements.txt
```

## Run with uvicorn

```
uvicorn main:app
```

## Build docker image

```
docker build . -t fullsnacktestengineer/gifweather:local
```

## Run docker container

```
docker run -p 8000:8000 fullsnacktestengineer/gifweather:local
```