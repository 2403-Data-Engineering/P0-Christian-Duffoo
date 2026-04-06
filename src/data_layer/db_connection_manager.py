import os
import mysql.connector

from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()



def get_connection():
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        port = os.getenv("PORT"),
        user = os.getenv("USER"),
        password = os.getenv("PASS"),
        db = os.getenv("DB"),
        autocommit = True
    )