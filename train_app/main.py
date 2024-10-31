import sys
from typing import Dict, Any
from PySide6.QtWidgets import QApplication

from windows import WindowsEngine
from layouts import Ui_MainWindow


class Main:
    """Отвечает за взаимодействие между окнами и данными

    АТРИБУТЫ:
    ---------
    engine    :    WindowsEngine - Объект который отвечает за работу всех окон

    МЕТОДЫ:
    -------

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------

    """

    def __init__(self):
        """"""
        self.engine = WindowsEngine(Ui_MainWindow)


class DataBase:
    """Осуществляет взаимодействие с базой данных

    АТРИБУТЫ:
    ---------

    МЕТОДЫ:
    -------
    get_info(self, query: str)\n
    insert_info(self, query)\n


    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------


    """

    def __init__(self):
        pass

    def get_info(self, query: str):
        pass

    def insert_info(self, query: str):
        pass


class User:
    """

    АТРИБУТЫ:
    ---------

    МЕТОДЫ:
    -------

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------


    """
    pass


class Passanger(User):
    """

    АТРИБУТЫ:
    ---------

    МЕТОДЫ:
    -------

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------


    """
    pass


class Driver(User):
    """

    АТРИБУТЫ:
    ---------

    МЕТОДЫ:
    -------

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------

    """
    pass


class Staff(User):
    """

    АТРИБУТЫ:
    ---------

    МЕТОДЫ:
    -------

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------


    """
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.engine.show_window("MainWindow")
    sys.exit(app.exec())
