import sys

from PySide6.QtWidgets import QApplication

#  Импорт форм окон
from windows import WindowsEngine
from layouts import Ui_Start, Ui_Profile

#  Имопрт скрипта для обновления ui файлов (УДАЛИТЬ ПОЗЖЕ)
# import convet_ui_files


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
        self.engine = WindowsEngine(Ui_Profile,
                                    Ui_Start,
                                    )


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
    main.engine.show_window(all_windows=True)
    sys.exit(app.exec())
