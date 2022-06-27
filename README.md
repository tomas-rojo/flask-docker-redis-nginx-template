# Docker Template to work with Flask web app, Nginx load balancer and Redis

## Clone the Repo:

```
git clone https://github.com/tomas-rojo/flask-docker-redis-nginx-template.git flask_app
```

## Enter to Directory:

```
cd flask_app
```

## Start Docker:

```
docker-compose up -d --build 
```

## Or start Docker with multiple servers (eg. 3):

```
docker-compose up -d --build --scale flask_app=3
```
