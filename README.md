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
The gateway will be serve on a FastAPI application. [Code](gateway.py)
## Run the gateway
```sh
uvicorn gateway:app --reload
```
# Proto
Working on [proto.py](proto.py)