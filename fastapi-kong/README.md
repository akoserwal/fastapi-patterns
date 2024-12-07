# How to register FastAPI service with Kong API Gateways

## Run Docker compose setup

```KONG_DATABASE=postgres docker compose --profile database up -d```

## Docker Build and Run FAST API application

docker build -t my-fastapi-app .
docker run -d -p 8000:8000 my-fastapi-app

## Test API endpoint

```curl -i -X GET \
--url http://localhost:8000/api/hello \
--header 'Host: localhost'
```
