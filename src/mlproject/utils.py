import os
import sys
import pandas as pd
import pymysql

from dotenv import load_dotenv
from mlproject.exception import CustomException
from mlproject.logger import logging


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():

    logging.info("Reading SQL database started")

    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )

        logging.info("Connection established")

        df = pd.read_sql_query("SELECT * FROM studentsperformance", mydb)

        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex, sys)
