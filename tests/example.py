import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Profile import Ui_MainWindow


def create_class(name_file):
    class Window(QMainWindow, name_file):

        def __init__(self):
            super().__init__()
            self.setupUi(self)

        @staticmethod
        def insert_info(**name_widgets: str):
            """Вставляет информацию в виджеты"""
            for widget, value in name_widgets.items():
                widget.setText(value)

        def get_info(self, *name_widgets: str) -> Dict[str, Any]:
            """Возвращает информацию из виджет"""
            return {name: self.__dict__[name].text() for name in name_widgets}

        def clear_windget(self, name_widget: str):
            """Очищает выбранные виджеты"""
            pass

    return Window


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # main = Window()
    # main.show()
    # sys.exit(app.exec_())
    a = A()
    a.test1()
