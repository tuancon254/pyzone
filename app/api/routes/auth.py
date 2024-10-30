from fastapi import APIRouter, Depends, status, HTTPException
from app.schemes import CreateUser, ResponseToken
from app.database import SessionLocal
from app.models import User
from datetime import datetime
from passlib.context import CryptContext
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt

auth = APIRouter(prefix='/auth', tags=['auth'])

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY= '8e9bcc90e06e2531121de6e1e1ddfc43fb6e9a00f2de8469d65b83e246e5dcdb'
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRE= 30

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return True

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else: 
         expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_hash_password(plain_password) -> str:
    return pwd_context.hash(plain_password)


@auth.post('/register', status_code=status.HTTP_201_CREATED)
async def register(db: db_dependency, user: CreateUser):
    create_user = User(
        username=user.username,
        password=get_hash_password(user.password),
        email=user.email,
        is_active=user.is_active,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        phone_number=user.phone_number
    )
    
    db.add(create_user)
    db.commit()
    
    return create_user


@auth.post('/token', response_model=ResponseToken)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency) -> ResponseToken:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    access_token = create_access_token(data={"sub": form_data.username}, expires_delta=access_token_expires)
    
    return ResponseToken(access_token=access_token, token_type="bearer")


@auth.get("/test")
async def test():
    return {"message": "It's worked"}

