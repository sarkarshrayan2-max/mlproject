import os
import sys
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")

def read_sql_data():
    logging.info("Reading data from mysql database")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,database=database)
        logging.info("Successfully connected to the database")
        df=pd.read_sql("SELECT * FROM students",mydb)
        print(df.head())
        return df
    except Exception as e:
        raise CustomException(e, sys)