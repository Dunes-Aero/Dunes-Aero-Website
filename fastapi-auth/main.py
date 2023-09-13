from fastapi import Depends, FastAPI, HTTPException, Request,Body,status
from auth.jwt_auth import authenticate_user, create_access_token, get_hashed_password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.models import Token, User
from fastapi.middleware.cors import CORSMiddleware
from db.crud import searchUser, create_connection,create_table,loginUser, addUser, getUser
import json
from datetime import datetime, timedelta
from auth.models import TokenData
from jose import JWTError
import jwt
from jwt.exceptions import ExpiredSignatureError
from pydantic import BaseModel
from passlib.context import CryptContext
from db.crud import create_connection, create_table, searchUser


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
ACCESS_TOKEN_EXPIRE_MINS = 30

#create db connection and prepare table
try:
    conn = create_connection('users.db')
    create_table(conn)
except Exception:
   print("Error had occured")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: Move to .env file
SECRET_KEY = "59441d59c8c290485ada1d983ae755e8"
ALGORITHM = "HS256"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/login/")
async def root(payload: dict = Body(...)):
    email = payload["email"]
    password = payload["password"]
    try:
      user = getUser(con=conn, email=email)

      if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password", 
                            headers={"WWW-Authenticate": "Bearer"})
      token = await generate_token(email,password)
      print("dtaaaaaaaaaaaaaaaaaaaaaaaaaaa:{}".format(token))
      data = token.copy()
      
      data.update({'name':user.name})
      return {'status':200, 'data':data}
    except Exception as e :
        print("lagin error :{}".format(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unexpected authentication error", 
                            headers={"WWW-Authenticate": "Bearer"})
    


#check the db 
@app.post("/signup/")
async def root(payload: dict = Body(...)):
    name = payload["name"]
    email = payload["email"]
    password = payload["password"]
    try:
      user  = getUser(email,con=conn)
    
      if not user:
         hashed_password = get_hashed_password(password)
         addUser(conn,name,hashed_password,email)
         token = await generate_token(email,password)
         return token
      else  :
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password", 
                            headers={"WWW-Authenticate": "Bearer"})
    except:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unexpected authentication error", 
                            headers={"WWW-Authenticate": "Bearer"})
    
async def generate_token(email,password):
    print("att tooooooken")
    user = authenticate_user(con=conn, email=email, password=password)
    print("att tooooooken userrrrrrrrr:{}".format(user))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password", 
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expire= timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)
    access_token = create_access_token(data={"sub": user.email}, expire_delta=access_token_expire)
    return {"access_token": access_token, "token_type":"bearer"}

@app.post("/token", response_model=Token)
async def token(payload: dict = Body(...)):
    email = payload["email"]
    password = payload["password"]
    user = authenticate_user(con=conn, email=email, password=password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password", 
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expire= timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)
    access_token = create_access_token(data={"sub": user.email}, expire_delta=access_token_expire)
    return {"access_token": access_token, "token_type":"bearer"}



#TODO: Delete this after finsihing tests
# def test_get(token: str = Depends(oauth2_scheme)):
#    print("token is test get is :{}".format(token))
#    payload=""
#    try:

#     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     print("decoded  {}".format(payload.get("sub")))
#    except Exception as e:
#       raise Exception("something baaaaaaaaaaad occured")
#    return {"data":"yahoooo"}




#The function will be locked, unless an authorization token is specified in the header
#it should return the user by the email returned from decoding the token
async def get_current_user(token: str= Depends(oauth2_scheme)):
    #Craft the HTTP exception
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    email=''
    #Decode the access token which should contain only an email field
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        if email is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    except  ExpiredSignatureError:
        raise credential_exception
    #Get the user linked to the email
    user = getUser(con=conn, email=email)
    if user is None:
        raise credential_exception


    
    return user
#the authrozation header should contain a token
@app.post("/get_user")
async def get_user(user: dict= Depends(get_current_user)):
   try: 
    return user
   except Exception as e :
      print("error in get_user route {}".format(e))


   




   



