from fastapi import FastAPI, Request,Body
from fastapi.middleware.cors import CORSMiddleware
from db.crud import searchUser, create_connection


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

#create db connection 
conn = create_connection('users.db')

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/main")
async def root():
    return {"message": "Hello main"}

@app.get("/login/")
async def root(payload: dict = Body(...)):

    return payload
    print("request for login : {}".format(data))
    return {"status":200, "msg":"yaho"}
    print("request for login : {}".format(request))
    email="email"
    password="password"
    try:
      res = searchUser(email,password)
      if (res == None):
        return {'status':400, 'msg':'Invlaid email or password'}
      else:
        return {'status':200, 'data':res}
    except:
        return {'status':500, 'msg':'Unexpected error had occured'}

