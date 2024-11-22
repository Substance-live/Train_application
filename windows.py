import sys
from typing import Dict, Any
import PySide6.QtWidgets as QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt


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

    def disable_window(self, bool_atr: bool, *name_windows: str, all_windows=False):
        """Блокировка выбранных окон"""

        #  Проверка name_windows
        assert set(name_windows).issubset(self.windows.keys()), 'Имя окна не найдено'

        if all_windows:
            for window in self.windows.values():
                window.setDisabled(bool_atr)
        else:
            for name in name_windows:
                self.windows[name].setDisabled(bool_atr)

    def hide_window(self, *name_windows: str, all_windows=False):
        """Скрывает выбранные окна"""

        #  Проверка name_windows
        assert set(name_windows).issubset(self.windows.keys()), 'Имя окна не найдено'

        if all_windows:
            for window in self.windows.values():
                window.hide()
                window.clear_windget(all_widgets=True)
        else:
            for name in name_windows:
                self.windows[name].hide()
                self.windows[name].clear_windget(all_widgets=True)

    def show_window(self, *name_windows: str, all_windows=False, hide_windows=True):
        """Отображает выбранные окна"""

        #  Проверка name_windows
        assert set(name_windows).issubset(self.windows.keys()), 'Имя окна не найдено'

        #  Сокрытие всех окон
        if hide_windows:
            self.hide_window(all_windows=True)

        if all_windows:
            for window in self.windows.values():
                window.show()
        else:
            for name in name_windows:
                self.windows[name].show()

    def get_widget(self, name_window: str, name_widget: str) -> Any:
        """Возвращает объекта виджета для точечной настройки"""

        assert hasattr(self.windows[name_window], name_widget), "Неверное имя виджета"

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

            def set_focus_event(self, widget, function):
                """Назначить виджету функцию при появлении фокуса на нам"""

                self.__dict__[widget].focusInEvent = function

            def mousePressEvent(self, event):
                """Перегружаем метод нажатия на пустое место в окне для сброса фокуса"""

                if event.button() == Qt.MouseButton.LeftButton:
                    self.clearFocus()  # Сбрасываем фокус со всех виджетов
                    self.setFocus()  # Устанавливаем фокус на окно

            def insert_info(self, **name_widgets: str):
                """Вставляет информацию в виджеты"""

                #  Проверка name_widgets
                assert set(name_widgets.keys()).issubset(self.__dict__.keys()), "Неверное имя виджета"

                for widget, value in name_widgets.items():
                    self.__dict__[widget].setText(value)

            def get_info(self, *name_widgets: str) -> Dict[str, any]:
                """Возвращает информацию из виджет"""

                #  Проверка name_widgets
                assert set(name_widgets).issubset(self.__dict__.keys()), "Неверное имя виджета"

                return {name: self.__dict__[name].text() for name in name_widgets}

            def clear_windget(self, *name_widgets: str, all_widgets=False):
                """Очищает выбранные виджеты"""
                if all_widgets:
                    for widget in self.__dict__.keys():

                        if (isinstance(self.__dict__[widget], QtWidgets.QLineEdit)
                                and hasattr(self.__dict__[widget], 'clear')):
                            self.__dict__[widget].clear()

                        elif (isinstance(self.__dict__[widget], QtWidgets.QCheckBox)
                              and hasattr(self.__dict__[widget], 'setChecked')):
                            self.__dict__[widget].setChecked(False)

                else:
                    for widget in name_widgets:
                        self.__dict__[widget].clear()

        return Window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowsEngine()
    sys.exit(app.exec())
