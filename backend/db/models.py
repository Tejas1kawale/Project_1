#This file will have the what kind of data is going to be inserted in the database
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import INTEGER,String,Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(INTEGER,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbArticle',back_populates='user')

class DbArticle(Base):
    __tablename__ = 'articles' # type: ignore
    id = Column(INTEGER,primary_key=True,index=True)
    task = Column(String)
    description = Column(String)
    user_id = Column(INTEGER,ForeignKey('users.id'))
    user = relationship('DbUser',back_populates='items')
    
    
    