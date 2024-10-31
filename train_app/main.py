import sys
from typing import Dict, Any
from PySide6.QtWidgets import QApplication, QMainWindow
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

        self.engine.show_window("MainWindow")


class WindowsEngine:
    """Отвечает за удобную работу с окнами

    АТРИБУТЫ:
    ---------


    МЕТОДЫ:
    -------
    hide_window
    show_window
    create_window

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------


    """

    def __init__(self, *windows: Any):
        """Создание экземпляра каждого окна"""
        self.windows = {str(name_class)[str(name_class).find('Ui')+3:-2]:
                        self.create_window(name_class)() for name_class in windows}

    def hide_window(self, *name_windows: str):
        """Скрывает выбранные окна"""
        for name in name_windows:
            self.windows[name].hide()

    def show_window(self, *name_windows: str):
        """Отображает выбранные окна"""
        for name in name_windows:
            self.windows[name].show()

    @staticmethod
    def create_window(name_file: Any):
        """Создает уникальный класс по преобразованному ui файлу в переменной name_file"""

        class Window(QMainWindow, name_file):
            """Отдельный класс под каждое окно программы

            Хранит всю информацию виджетах

            АТРИБУТЫ:
            ---------
            Отдельные для каждого окна

            МЕТОДЫ:
            -------
            insert_info
            get_info
            clear_windget

            ПРИМЕЧАНИЕ:
            -----------

            ОШИБКИ:
            -------


            """

            def __init__(self):
                super().__init__()
                self.setupUi(self)

            def insert_info(self, **name_widgets: str):
                """Вставляет информацию в виджеты"""
                for widget, value in name_widgets.items():
                    self.__dict__[widget].setText(value)

            def get_info(self, *name_widgets: str) -> Dict[str, any]:
                """Возвращает информацию из виджет"""
                return {name: self.__dict__[name].text() for name in name_widgets}

            def clear_windget(self, *name_widgets: str):
                """Очищает выбранные виджеты"""
                for widget in name_widgets:
                    self.__dict__[widget].clear()

        return Window


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
    sys.exit(app.exec())
