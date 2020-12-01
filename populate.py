# UTF8
# Date: 26 Nov.
# Author: Margaux Faurie


import json
import datetime
from connection import connect
from random import shuffle
from models import Books


def populate(dbname, jsondata):
    """docstring for populate"""
    session = connect(dbname)

    with open(jsondata) as f:
        data = json.load(f)

    for i in data['books']:
        book_data = Books(Title = i["Title"], Author = i["Author"], ReadOrNot = "0")
        session.add(book_data)
    session.commit()

