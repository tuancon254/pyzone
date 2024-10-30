from fastapi import FastAPI
from app.models import Base
from app.database import engine
from api.routes.auth import auth
# Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth)
