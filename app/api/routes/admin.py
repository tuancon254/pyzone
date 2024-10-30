from fastapi import APIRouter
from app.schemes import User

admin = APIRouter(prefix='/admin', tags=['admin'])

