from datetime import datetime, timedelta
import time
from fastapi import Depends, HTTPException, status
from auth.models import TokenData, User
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import jwt
from pydantic import BaseModel
from passlib.context import CryptContext
from db.crud import create_connection, create_table, getUser


# TODO: Move to .env file
SECRET_KEY = "59441d59c8c290485ada1d983ae755e8"
ALGORITHM = "HS256"






pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Valdited a plain password against its claimed hashed one
def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

#Apply hashing algorithm to an input password
def get_hashed_password(password):
    try:
      hash=  pwd_context.hash(password)
      return hash
    except Exception as e:
        print("Error in password hashing {}".format(e))
        return password

#This function Should return User object if the email and password were authnticated, otherwise it would return false 
def authenticate_user(con, email: str, password: str):
    user = getUser(email=email, con=con)
    if not user :
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expire_delta: timedelta or None = None):
    #At this point, the data only has 'sub' field, which contains the user smail
    to_encode = data.copy()
    #Use the sepsified expiry duration, otherwise set it to 15 mins
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    #the returned token should contain the email and expiry date
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# #Get current user from a given token 
# async def get_current_user(con, token: str= Depends(oauth2_scheme)):
#     #Craft the HTTP exception
#     credential_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Invalid credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email:str = payload.get("sub")
#         if email is None:
#             raise credential_exception
#         token_data = TokenData(email=email)
#     except JWTError:
#         raise credential_exception
#     user = getUser(con=con, email=token_data.email)
#     if user is None:
#         raise credential_exception
    
#     return user


# #TODO: add user activity feature later
# async def get_current_active_user(current_user:User):
#     pass
