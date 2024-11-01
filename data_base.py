from pymysql import connect, Error
import os
from dotenv import load_dotenv
from typing import Any


class DataBase:
    """Отвечает за взаимодействие между окнами и данными

        АТРИБУТЫ:
        ---------
        DB_HOST    :   str - Хост сервера базы данных\n
        DB_USER    :   str - Имя пользователя базы данных\n
        DB_PASSWORD    :   str - Пароль к базе данных\n
        DB_NAME    :   str - Имя базы данных\n

        connection   :   PyMySQL.connection - Хранит объект для работы с БД\n

        МЕТОДЫ:
        -------
        connect_to_base(self) -> connect - Осуществляет подключение к базе данных\n
        update_data(self, query: str) - Вставляет, удаляет или обновляет данные в соответствии с запросом\n
        get_data(self, query: str, single_line=False) -> Any - Возвращает результат запроса SQL\n

        ПРИМЕЧАНИЕ:
        -----------

        ОШИБКИ:
        -------

        """

    def __init__(self):
        load_dotenv()
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_NAME = os.getenv('DB_NAME')

        self.connection = self.connect_to_base()

    def connect_to_base(self) -> connect:
        """Осуществляет подключение к базе данных"""
        try:
            base = connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                db=self.DB_NAME,
                password=self.DB_PASSWORD,
            )

            print('Соединение установленно')
            return base

        except Error as message:
            raise message

    def update_data(self, query: str):
        """Вставляет, удаляет или обновляет данные в соответствии с запросом"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)

            self.connection.commit()

        except Error as message:
            raise message

    def get_data(self, query: str, single_line=False) -> Any:
        """Возвращает результат запроса SQL"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)

                #  Проверка параметра single_line
                if single_line:
                    ret = cursor.fetchall()
                else:
                    ret = cursor.fetchall()

            return ret

        except Error as message:
            raise message


if __name__ == '__main__':
    con = DataBase()
