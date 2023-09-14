from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email:str or None = None


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str