from fastapi import APIRouter, Depends, status, HTTPException
from schemes import CreateUser, ResponseToken
from database import SessionLocal
from models import User
from typing import Annotated
from sqlalchemy.orm import Session

document = APIRouter(prefix='/document', tags=['document'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


