from fastapi import FastAPI
from models import Base
from database import engine
from api.routes.admin import router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router)
