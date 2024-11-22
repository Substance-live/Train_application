import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Centered QTableWidget Example")
        self.setGeometry(100, 100, 400, 300)

        # Создаем основной виджет
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Создаем вертикальный слой для размещения элементов
        layout = QVBoxLayout()

        # Создаем QTableWidget
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)  # Устанавливаем количество столбцов
        self.table_widget.setHorizontalHeaderLabels(["Name", "Age", "Occupation"])  # Заголовки столбцов

        # Пример данных для добавления
        data = [
            ("Alice", 25, "Designer"),
            ("Bob", 30, "Developer"),
            ("Charlie", 22, "Artist"),
        ]

        # Заполняем таблицу данными и выравниваем по центру
        for row_data in data:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)

            for column_index, item in enumerate(row_data):
                table_item = QTableWidgetItem(str(item))  # Создаем элемент
                table_item.setTextAlignment(Qt.AlignCenter)  # Устанавливаем выравнивание по центру
                self.table_widget.setItem(row_position, column_index, table_item)  # Добавляем элемент в таблицу

        layout.addWidget(self.table_widget)  # Добавляем таблицу на слой
        main_widget.setLayout(layout)

# Запускаем приложение
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())