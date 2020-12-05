# UTF8
# Date: 26 Nov. 15h39
# Author: Margaux Faurie

import json
from sqlalchemy.orm import sessionmaker, query
from connection import connect, createdb, checkdb
from datetime import datetime
from createtables import createtables
from populate import populate
import sqlalchemy as db
from models import Books
import pandas as pd

# ----------------------------
# Create the database --> C
# ----------------------------

startTime = datetime.now() #Take the time to know how long the set up lasted
print('\n\n----------------------------------------------------')
print("Setup in progress. Please wait.")
print('----------------------------------------------------\n')

dbname = 'booklist' #Name the database
rawdata = 'data.json' #Where does the raw data comes from


with open("config.json") as f: #Load data for the configuration
        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

def Checkdb(dbname):
    prgrm = 1
    if checkdb(dbname) is True: #Check the existance of the database (if exists or not)
        createdb(dbname) #Create the database
        session = connect(dbname) #Connect to the database

        createtables(dbname) #Create the tables
        populate(dbname, rawdata) #Populate the database

        finishTime = datetime.now() #End of the set up
        timeDetla = finishTime - startTime

        print('\n----------------------------------------------------')
        print("Setup is finished. Your database is now available.")
        print("The process was completed in : " + str(
            timeDetla.total_seconds()) + "s.") #Total time
        print('----------------------------------------------------\n')
        return prgrm
       else:
        print("Your database already exists.\n")
        print('Here are the tables and their columns that exists : ')

        engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
        connection = engine.connect() #Connect
        session = connect(dbname) #Connect to the database

        metadata = MetaData(bind = engine)

        m = MetaData()
        m.reflect(engine)
        for table in m.tables.values():
            print("Table name: ", table.name, "\n")
            for column in table.c:
                print("Column name: ", column.name)

        print('\nDo you want to see what is inside a specific table ? ')
        print('1 = You want to see inside a table.')
        print('Other integer : do not show anything')
        print('Which table do you want to see ? \n')
        
        try: 
            choice = int(input('Your choice : '))
        except ValueError:
            print('The input is not right. We will consider you do not want to see anything\n')
            choice = 0
        
        if choice == 1:
            print('You asked to see what is inside a database. Which one do you want to see ? ')
            databasechosen = str(input('Your choise :' ))
            print(pd.DataFrame(connection.execute("SELECT * FROM {}".format(databasechosen)))
        else:
            pass

        print('Do you want to add the data that does not exist (without deleting the previously existing one ?')
        print('1 = You want to add the data and run the program')
        print('Other integer : do not do anything : the program will stop')


        try:
            Choice = int(input('Your choice : '))
        except ValueError:
            print("The input is not right... We will consider you do not want the program to run.\n")
            prgrm = 0
            return prgrm

        if Choice == 1:
            session = connect(dbname)

            with open('data.json') as f:
                data = json.load(f)

            for i in data['books']:
                exists = db.session.query(Books.title).filter_by(Title = '{}'.format(i["Title"])).scalar() is not None #Check if the data exists
                if exists == None: #If the data does not exist, it is implemented
                    session.add(Books(Title = i["Title"], Author = i["Author"], ReadOrNot = "0"))  
                else: #It the book already exists, it is not added
                    pass
            session.commit
            return prgrm #The program will run properly

        else : 
            prgrm = 0
            print('The program will not run')
            return prgrm

        print('----------------------------------------------------\n')

prgrm = 1 
prgrm = Checkdb(dbname)
if prgrm == 1:
    # ---------------------------------
    # How to read a table ?  --> R
    # ---------------------------------

    engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
    connection = engine.connect() #Reconnect to the database

    def printtable(connection): # Def a function that print a database using pandas
        return pd.DataFrame(connection.execute("SELECT * FROM books"))

    print("\nOriginal database:\n")
    print(printtable(connection))
    print('\n----------------------------------------------------\n')


    # ---------------------------
    # Update book  --> U
    # ---------------------------
    print('Which book have you read ?')
    
    bookupdate = str(input('Book Title: '))
    query = db.update(Books).values(ReadOrNot="1").where(Books.Title=="{}".format(bookupdate))


    results = connection.execute(query)

    print("\nDatabase with update:\n")
    print(printtable(connection))
    print('\n----------------------------------------------------\n')


    # ------------------------------------------------------
    # Suppresion du livre lu "The World as I See It" --> D
    # ------------------------------------------------------

    query = db.delete(Books).where(Books.Title == "{}".format(bookupdate))
    results = connection.execute(query)

    print("Database with deleted element:\n")
    print(printtable(connection))
    print('\n\n----------------------------------------------------')
    print('CRUD Complete')
    print('----------------------------------------------------\n')
else:
    print('You asked not to run the program')


