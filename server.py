from mysql.connector import connect, Error
from dotenv import load_dotenv
from collections import namedtuple
import os

load_dotenv()

connection = connect(
    host=(os.getenv("SERVER")),
    port=(os.getenv("PORT")),
    user=(os.getenv("USERNAME")),
    password=(os.getenv("PASSWORD")),
    database=(os.getenv("NAME"))
) 

get_db_connection = lambda autocommit=False: connect(
     host=(os.getenv("SERVER")),
    port=(os.getenv("PORT")),
    user=(os.getenv("USERNAME")),
    password=(os.getenv("PASSWORD")),
    database=(os.getenv("NAME")),
    autocommit = autocommit
) 

print(connection.is_connected())
 
connection.close()

