from pydantic import BaseModel
from typing import List


#article inside 
class Article(BaseModel):
    task : str
    description : str
    class Config():
        orm_mode = True
        
class User(BaseModel):
    id: int
    username:str

class userBase(BaseModel):
    username: str
    email: str
    password: str

class userDisplay(BaseModel):
    username: str
    email:str
    items: List[Article] = []
    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    task :str
    description:str
    creater_id: int
    
class ArticleDsiplay(BaseModel):
    task:str
    description:str
    user: User
    class Config():
        orm_mode = True
    