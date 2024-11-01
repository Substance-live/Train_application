import pymysql
import os
from dotenv import load_dotenv


class DataBase:

    def __init__(self):
        load_dotenv()
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_NAME = os.getenv('DB_NAME')

        self.conection = self.connect_to_base()

    def connect_to_base(self):
        try:
            base = pymysql.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                db=self.DB_NAME,
                password=self.DB_PASSWORD,
            )

            print('Соединение установленно')
            return base

        except pymysql.Error as e:
            raise e


if __name__ == '__main__':
    con = DataBase()
