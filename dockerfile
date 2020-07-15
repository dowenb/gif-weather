ARG TAG=3.8-alpine3.12_2020-07-07_31a0aaa
FROM midnighter/fastapi-base:${TAG}
COPY . /app
WORKDIR /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]