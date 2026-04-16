#backend/routes/deployments.py
from fastapi import APIRouter, HTTPException
from models import  Deployment, DeploymentsCreate
from typing import Literal
import uuid
from datetime import datetime
# qual router vou usar para criar as rotas de deployments?
router = APIRouter()
#lista de deployments para armazenar os dados em memória
deployments: list[Deployment] = []

# Rota 1: Tentando listar todos os deployments
@router.get("/deployments", response_model=list[Deployment])
def get_deployments():
    return deployments
# Rota 2: Criar um novo deployment
@router.post("/deployments", response_model=Deployment) 
def create_deployment(data: DeploymentsCreate):
    new = Deployment(
        id=str(uuid.uuid4()),
        name=data.name,
        status="stopped",
        created_at=datetime.now().isoformat()
    )
    deployments.append(new)
    return new

# Rota 3: mudar o estado do deployment
@router.patch("/deployments/{deployment_id}/status")
def update_status(deployment_id: str, status: Literal["running", "stopped", "error"]):
    for dep in deployments:
        if dep.id == deployment_id:
            dep.status = status
            return dep
    raise HTTPException(status_code=404, detail="Deployment not found")