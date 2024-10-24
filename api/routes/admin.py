from fastapi import APIRouter
from schemes import User

admin = APIRouter(prefix='/admin', tags=['admin'])

