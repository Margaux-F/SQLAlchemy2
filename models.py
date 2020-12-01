# UTF8
# Date: 26 Nov.
# Author: Margaux Faurie

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from connection import connect

session = connect('aam_test_301')

Base = declarative_base()



class Books(Base):
    """docstring for """
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, nullable = False)
    Title = Column(String(20), nullable = True)
    Author = Column(String(100), nullable = True)
    ReadOrNot = Column(String(1), nullable = True)

