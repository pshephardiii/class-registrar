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

def reset():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            with open('tables.sql', 'r') as f:
                for result in cursor.execute(f.read(), multi=True):
                    pass

    connection.close()

def add_a_student(first_name, last_name, unix_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students (first_name, last_name, unix_id) VALUES (%s, %s, %s);",
                (first_name, last_name, unix_id))
            conn.commit()
