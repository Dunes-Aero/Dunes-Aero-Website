from fastapi import FastAPI, Request,Body
from fastapi.middleware.cors import CORSMiddleware
from db.crud import searchUser, create_connection,create_table,loginUser, addUser
import json


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

#create db connection and prepare table
try:
    conn = create_connection('users.db')
    create_table(conn)
except Exception:
   print("Error had occured")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/main")
async def root():
    return {"message": "Hello main"}

@app.post("/login/")
async def root(payload: dict = Body(...)):
    email = payload["email"]
    password = payload["password"]
    try:
      res = loginUser(email,password, con=conn)
      if (res == None):
        return {'status':400, 'msg':'Invlaid email or password'}
      else:
        return {'status':200, 'data':res}
    except:
        return {'status':500, 'msg':'Unexpected error had occured'}
    



@app.post("/signin/")
async def root(payload: dict = Body(...)):
    print("request for sign in : {}".format(payload))
    name = payload["name"]
    email = payload["email"]
    password = payload["password"]
    try:
      res = searchUser(email,con=conn)
       
      if res is not None:
        return {'status':400, 'msg':'Invlaid email or password'}
      else:
         addUser(conn,name,password,email)
         return {'status':200, 'data':'new user'}
                    
    except:
        return {'status':500, 'msg':'Unexpected error had occured'}

