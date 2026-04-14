# backend / main.py criado para iniciar o servidor fastapi e definir as rotas da API
from fastapi import FastAPI

app = FastAPI()
deployments = [
    {"id": 1, "name": "Deployment 1 - Site A", "status": "rodando"},
    {"id": 2, "name": "Deployment 2 - Site B", "status": "parado"},
    {"id": 3, "name": "Deployment 3 - Site C", "status": "erro"},
    {"id": 4, "name": "Deployment 4 - Site D", "status": "rodando como pião de guerra"},
]

@app.get ("/deployments")
def get_deployments():
    return deployments