# backend / main.py criado para iniciar o servidor fastapi e definir as rotas da API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import deployments 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deployments.router)

