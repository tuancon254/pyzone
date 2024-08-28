from fastapi import FastAPI, APIRouter

router = APIRouter(prefix='/admin', tags=['admin'])

@router.get('/')
def index():
    return {'message': '1'}

