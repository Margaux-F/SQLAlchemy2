# UTF8
# Date: 26 Nov.
# Author: Margaux Faurie

import json
from urllib.request import urlopen
import sqlalchemy as al
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine, update
from sqlalchemy_utils import create_database, database_exists


def checkdb(name):
    with open("config.json") as f:
        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

        if not database_exists(
                f'mysql+pymysql://{username}:{password}@{host}/{name}'):
            return True
        else:
            return False


def createdb(name):
    """create DB in mysql named: 'name variable' """
    with open("config.json") as f:
        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

        create_database(f'mysql+pymysql://{username}:{password}@{host}/{name}')
        print("This database din't exist. Creation in process. Please wait.")


def connect(name):
    """Connect Python to the MySQL database with: 'name variable' """
    with open("config.json") as f:

        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

        engine = create_engine(
            f'mysql+pymysql://{username}:{password}@{host}/\
{name}?host={host}?port={port}',
            echo=False, encoding='utf8', pool_recycle=60000,
            pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        return session


def engine(name):
    """returns database's engine with: 'name variable' """
    with open("config.json") as f:

        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

        engine = create_engine(
            f'mysql+pymysql://{username}:{password}@{host}/\
{name}?host={host}?port={port}',
            echo=False, encoding='utf8', pool_recycle=60000,
            pool_pre_ping=True)

        return engine
