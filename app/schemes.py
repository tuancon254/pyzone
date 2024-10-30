from pydantic import BaseModel, Field
from typing import Annotated
from fastapi import Query

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=16)
    password: Annotated[str | None, Query(max_length=50)]

class CreateUser(User):
    email: Annotated[str | None, Query(max_length=50)]
    is_active: bool = True
    phone_number: Annotated[str | None, Query(max_length=16)]

class Token(BaseModel):
    token: str 
    
class ResponseToken(BaseModel):
    access_token: str
    token_type: str 