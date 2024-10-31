import sys
from typing import Dict, Any
from PySide6.QtWidgets import QApplication, QMainWindow


class WindowsEngine:
    """Отвечает за удобную работу с окнами

    АТРИБУТЫ:
    ---------
    self._windows    :   Dict[str, Window] - Словарь с окнами (Ключ название Ui файла без префикса,
    например Ui_Window1 -> Window1)

    МЕТОДЫ:
    -------
    hide_window(self, *name_windows: str) - Скрывает выбранные окна\n
    show_window(self, *name_windows: str) - Отображает выбранные окна\n
    create_window(name_file: Any) - Создает уникальный класс по преобразованному ui файлу в переменной name_file\n
    get_widget(self, name_window: str, name_widget: str) -> QWidget -
    Возвращает объекта виджета для точечной настройки\n

    ОШИБКИ:
    -------
    Передача в функции в качества аргумента не существующие название окна

    """

    def __init__(self, *windows: Any):
        """Создание экземпляра каждого окна"""
        self.windows = {str(name_class)[str(name_class).find('Ui') + 3: -2]:
                        self.create_window(name_class)() for name_class in windows}

    def hide_window(self, *name_windows: str, all_windows=False):
        """Скрывает выбранные окна"""
        if all_windows:
            for window in self.windows.values():
                window.hide()
        else:
            for name in name_windows:
                self.windows[name].hide()

    def show_window(self, *name_windows: str, all_windows=False):
        """Отображает выбранные окна"""
        if all_windows:
            for window in self.windows.values():
                window.show()
        else:
            for name in name_windows:
                self.windows[name].show()

    def get_widget(self, name_window: str, name_widget: str) -> Any:
        """Возвращает объекта виджета для точечной настройки"""
        return self.windows[name_window].__dict__[name_widget]

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
            insert_info(self, **name_widgets: str) - Вставляет информацию в виджеты\n
            get_info(self, *name_widgets: str) -> Dict[str, any] - Возвращает информацию из виджет\n
            clear_windget(self, *name_widgets: str) - Очищает выбранные виджеты\n

            ОШИБКИ:
            -------
            При вызове функций с передачей виджета в виде аргумента, который не поддерживает данную операцию

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowsEngine()
    sys.exit(app.exec())
