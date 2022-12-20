# Enviroment
I'll use a conda enviroment for this project.
## Create a conda enviroment
```bash
conda create -n mlbookcamp python=3.9.15
```
## Activate the enviroment
```bash
conda activate mlbookcamp
```
## Install ipykernel
```bash
conda install ipykernel
```
## Install dependencies
```bash
pip install -r requirements.txt
```

# Gateway
The gateway will be serve on a Flask application. [Code](gateway.py)
## Run the gateway
```sh
gunicorn --bind=0.0.0.0:9696 gateway:app
```
# Proto
Working on [proto.py](proto.py)
# Docker-compose
## Gateway Dockerfile
I'll create a dockerfile for the gateway
```docker
FROM python:3.9.15

RUN pip install pipenv

WORKDIR /app 

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["gateway.py", "proto.py", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "gateway:app" ]
```
## Build Dockerfile
```sh
docker build -t kitchen-gateway:001 -f image-gateway.Dockerfile .
```