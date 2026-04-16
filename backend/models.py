# backend/models.py
from pydantic import BaseModel
from typing import Literal
import uuid
from datetime import datetime

class DeploymentsCreate(BaseModel):
    name: str

class Deployment(BaseModel):
    id: str
    name: str
    status: Literal["running", "stopped", "error"]
    created_at: str