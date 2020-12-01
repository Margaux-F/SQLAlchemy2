# UTF8
# Date: 26 Nov.
# Author: Margaux Faurie

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy import Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connection import engine

def createtables(name):
    """Create tables in OC Pizza DB"""
    Base = declarative_base()
    engin = engine(name)
    metadata = MetaData(bind = engin)

    books = Table(
        'books', metadata,
        Column('id', Integer, primary_key = True), 
        Column('Title', String(40), nullable = True),
        Column('Author', String(100), nullable = True),
        Column('ReadOrNot', String(1), nullable = True)
    )

    # Create all tables
    metadata.create_all(engin)

