from mysql.connector import connect, Error
from dotenv import load_dotenv
from collections import namedtuple
import os


load_dotenv()


def get_connection():
    connection = None
    try:
        connection = connect(
            host=(os.getenv("SERVER")),
            port=(os.getenv("PORT")),
            user=(os.getenv("USERNAME")),
            password=(os.getenv("PASSWORD")),
            database=(os.getenv("NAME"))
        ) 
    except Error as e:
        print(f"Error '{e}' occured while attempting to connect to the database")
    return connection


get_db_connection = lambda autocommit=False: connect(
    host=(os.getenv("SERVER")),
    port=(os.getenv("PORT")),
    user=(os.getenv("USERNAME")),
    password=(os.getenv("PASSWORD")),
    database=(os.getenv("NAME")),
    autocommit = autocommit
) 




