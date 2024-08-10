from fastapi import FastAPI, Depends
from db import models
from db.database import engine,get_db
from db.schemas import userBase,userDisplay,ArticleBase,ArticleDsiplay
from sqlalchemy.orm import Session
from db import db_user,db_task
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI ()

@app.get('/')
def index():
    return {'message '  :  'hello world'}


@app.get('/get_id/{id}')
def get_id(id:int):
    return {'Your id': f'{id}'}


@app.post("/create_user",response_model=userDisplay)
def create_user(request:userBase,db:Session = Depends(get_db)):
    return db_user.create_user(db,request)

@app.post('/create_task',response_model=ArticleDsiplay)
def creat_task(request:ArticleBase,db:Session= Depends(get_db)):
    return db_task.create_task(db,request)

@app.get('/get_task/{id}',response_model=ArticleDsiplay)
def get_task(id:int,db:Session= Depends(get_db)):
    return db_task.get_task(db,id)



origins = ['http://localhost:3000']


models.Base.metadata.create_all(engine)
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods = ["*"],
                   allow_headers = ["*"]
)
                   
                   
                   
                   