from db.models import DbArticle
from db.schemas import ArticleBase
from sqlalchemy.orm.session import Session


def create_task(db:Session,request:ArticleBase):
    new_task =  DbArticle(
        task = request.task,
        description = request.description,
        user_id = request.creater_id
    )  
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_task(db:Session,id:int):
    task = db.query(DbArticle).filter(DbArticle.id == id).first()
    return task

