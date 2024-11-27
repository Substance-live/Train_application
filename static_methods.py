import datetime

from PySide6.QtWidgets import QPushButton, QCheckBox, QMessageBox, QTableWidget, QTableWidgetItem, QComboBox, QDateEdit
from PySide6.QtCore import Qt

#  Импорт вспомогательных классов
from windows import WindowsEngine
from data_base import DataBase
from user import User


def get_rand_passwd() -> str:
    return "random_password"


class Check:

    @staticmethod
    def confirm_registr(but: QPushButton, check_confirm: QCheckBox):

        if check_confirm.isChecked():
            but.setEnabled(True)
        else:
            but.setEnabled(False)

    @staticmethod
    def change(combo_box: QComboBox, window, name_flag: str, items: list[str]):
        if window.__dict__[name_flag]:
            return

        window.__dict__[name_flag] = True

        text = combo_box.currentText().lower()

        filtered_items = [item for item in items if text in item.lower()]
        combo_box.clear()
        combo_box.addItems(filtered_items)

        combo_box.lineEdit().setText(text.capitalize())
        window.__dict__[name_flag] = False


class Show:

    @staticmethod
    def alter_login(engine: WindowsEngine):
        engine.show_window("FastLogin")

    @staticmethod
    def login(engine: WindowsEngine):
        engine.show_window("Login")

    @staticmethod
    def registr(engine: WindowsEngine):
        engine.show_window("Registr")

        #  Блокируем кнопку регистрации до подтверждение обработки данных
        engine.get_widget("Registr", "but_registr").setEnabled(False)

    @staticmethod
    def profile(engine: WindowsEngine):
        engine.show_window("Profile")

    @staticmethod
    def edit_profile(engine: WindowsEngine):
        engine.show_window("EditProfile")

        #  Блокируем кнопку регистрации до подтверждение обработки данных
        engine.get_widget("EditProfile", "but_save").setEnabled(False)

    @staticmethod
    def my_tickets(engine: WindowsEngine, db: DataBase, user: User):

        #  Загружаем данные из бд и подготавливаем переменную с таблицей
        data = Data.load_history(db, user)
        table: QTableWidget = engine.get_widget("MyTickets", "table")

        engine.show_window("MyTickets")

        #  Отключаем сортировку
        table.setSortingEnabled(False)

        for data_row in data:
            row_position = table.rowCount()

            # Вставляем новую строку в нижнюю часть таблицы
            table.insertRow(row_position)

            # Заполняем ячейки новыми данными
            for index in range(5):
                item = QTableWidgetItem(data_row[index])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, index, item)

        #  Включаем сортировку
        table.setSortingEnabled(True)

    @staticmethod
    def ticket(engine: WindowsEngine, db: DataBase):
        data = Data.load_tickets(db)
        stations = Data.get_stations(db)

        table: QTableWidget = engine.get_widget("Ticket", "table_timetable")
        combo_dep: QComboBox = engine.get_widget("Ticket", "combo_departure")
        combo_arr: QComboBox = engine.get_widget("Ticket", "combo_destination")

        engine.windows["Ticket"].flag_dep = False
        engine.windows["Ticket"].flag_arr = False

        combo_dep.addItems(stations)
        combo_arr.addItems(stations)

        engine.show_window("Ticket")

        #  Отключаем сортировку
        table.setSortingEnabled(False)

        for data_row in data:
            row_position = table.rowCount()

            # Вставляем новую строку в нижнюю часть таблицы
            table.insertRow(row_position)

            # Заполняем ячейки новыми данными
            for index in range(6):
                item = QTableWidgetItem(data_row[index])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, index, item)

        #  Включаем сортировку
        table.setSortingEnabled(True)


class Data:

    @staticmethod
    def logout(user: User):
        user.logout()

    @staticmethod
    def login(engine: WindowsEngine, db: DataBase, user: User, email: str, password: str):

        id_user = db.get_data("SELECT `idUser` "
                              "FROM `user` "
                              f"WHERE `email`='{email}' AND `password`='{password}'", single_line=True)
        if id_user is None:
            engine.get_widget("Login", "entry_passwd").clear()
            QMessageBox.information(engine.windows['Login'], "Ошибка авторизации",
                                    "Неверное имя пользователя или пароль", QMessageBox.Ok)
            return

        user.load_profile(id_user[0])
        QMessageBox.information(engine.windows['Login'], "Успешная авторизации",
                                "Авторизация прошла успешно", QMessageBox.Ok)
        Show.profile(engine)

    @staticmethod
    def registr(engine: WindowsEngine, db: DataBase, email: str):
        db.update_data(f"INSERT INTO `train`.`user` (`email`, `password`) VALUES ('{email}', '{get_rand_passwd()}');")

        QMessageBox.information(engine.windows['Registr'], "Успешная регистрация",
                                "Регистрация прошла успешно", QMessageBox.Ok)

    @staticmethod
    def send_message(engine: WindowsEngine, email: str):
        pass

    @staticmethod
    def edit_profile(db: DataBase, user: User, *args):
        db.update_data(f"UPDATE `train`.`user` "
                       f"SET `name` = '{args[0]}',"
                       f"`surname` = '{args[1]}',"
                       f"`patronymic` = '{args[2]}',"
                       f"`phone` = '{args[3]}',"
                       f"`birthday` = '{args[4]}' "
                       f"WHERE `idUser` = {user.id};")

    @staticmethod
    def load_history(db: DataBase, user: User) -> list[list[str]]:
        data = db.get_data(
            "SELECT t.`idTicket`, f.`title`, tt.`departure`, r.`price`, s.`title` "
            "FROM `ticket` as t "
            "JOIN `railcar` as r ON r.`idRailcar`=t.`idRailcar` "
            "JOIN `flight` as f ON f.`idFlight`=r.`idFlight` "
            "JOIN `list_status` as s ON s.`idStatus`=t.`idStatus` "
            "JOIN ( "
            "SELECT f.idFlight, MIN(tt.departure) as 'departure' "
            "FROM flight AS f "
            "JOIN timetable AS tt ON f.idFlight = tt.idFlight "
            "GROUP BY f.idFlight) as tt ON tt.idFlight = f.idFlight "
            f"WHERE t.`idUser`={user.id} "
            "ORDER BY t.`idTicket` "
        )

        ret = []
        for i in data:
            ret.append([str(i[0]), i[1], i[2].strftime("%Y-%m-%d"), str(i[3]), i[4]])

        return ret

    @staticmethod
    def cancel_ticket(engine: WindowsEngine, db: DataBase):
        table: QTableWidget = engine.get_widget("MyTickets", "table")
        row = table.currentRow()

        if table.item(row, 4).text() == "Подтверждён":
            db.update_data(
                "UPDATE `train`.`ticket` "
                "SET `idStatus` = 2 "
                f"WHERE `idTicket` = '{table.item(row, 0).text()}';"
            )
            QMessageBox.information(engine.windows['MyTickets'], "Билет изменён",
                                    "Билет успешно изменён", QMessageBox.Ok)
        else:
            QMessageBox.information(engine.windows['MyTickets'], "Ошибка отмены",
                                    "Данный билет нельзя вернуть", QMessageBox.Ok)

        table.setRowCount(0)

    @staticmethod
    def del_ticket(engine: WindowsEngine, db: DataBase):
        table: QTableWidget = engine.get_widget("MyTickets", "table")
        row = table.currentRow()

        if table.item(row, 4).text() in ("Отменён", "Завершен"):
            db.update_data(
                "DELETE FROM `train`.`ticket` "
                f"WHERE `idTicket` = '{table.item(row, 0).text()}';"
            )
            QMessageBox.information(engine.windows['MyTickets'], "Билет удалён",
                                    "Билет успешно удален", QMessageBox.Ok)
        else:
            QMessageBox.information(engine.windows['MyTickets'], "Ошибка удаления",
                                    "Данный билет нельзя удалить, попробуйте сначала его отменить", QMessageBox.Ok)

        table.setRowCount(0)

    @staticmethod
    def load_tickets(db: DataBase, *args, defualt=True) -> list[list[str]]:
        if defualt:
            data = db.get_data(
                "call tickets_common()"
            )
        else:
            data = db.get_data(
                f"call tickets_extended('{args[0].split()[0]}', '{args[1].split()[0]}', '{args[2].split('.')[2]}-{args[2].split('.')[1]}-{args[2].split('.')[0]}')"
            )

        ret = []
        for i in data:
            ret.append([i[1], i[2], i[3].strftime("%H:%M"), i[4].strftime("%H:%M"), str(int(i[5])), str(i[6])])

        return ret

    @staticmethod
    def get_stations(db: DataBase) -> list[str]:
        data = db.get_data("SELECT * FROM station")

        ret = []
        for i in data:
            ret.append(f"{i[1]} {i[2]}")

        return ret

    @staticmethod
    def reload_timtable(db: DataBase, engine: WindowsEngine):

        table: QTableWidget = engine.get_widget("Ticket", "table_timetable")
        combo_dep: QComboBox = engine.get_widget("Ticket", "combo_departure")
        combo_arr: QComboBox = engine.get_widget("Ticket", "combo_destination")
        date_edit: QDateEdit = engine.get_widget("Ticket", "date_edit")

        table.setRowCount(0)

        if combo_dep.lineEdit().text() == '' or combo_arr.lineEdit().text() == '':
            data = Data.load_tickets(db)
            #  Отключаем сортировку
            table.setSortingEnabled(False)

            for data_row in data:
                row_position = table.rowCount()

                # Вставляем новую строку в нижнюю часть таблицы
                table.insertRow(row_position)

                # Заполняем ячейки новыми данными
                for index in range(6):
                    item = QTableWidgetItem(data_row[index])
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row_position, index, item)

            #  Включаем сортировку
            table.setSortingEnabled(True)
            return

        data = Data.load_tickets(db,
                                 combo_dep.lineEdit().text(),
                                 combo_arr.lineEdit().text(),
                                 date_edit.lineEdit().text(),
                                 defualt=False)

        #  Отключаем сортировку
        table.setSortingEnabled(False)

        for data_row in data:
            row_position = table.rowCount()

            # Вставляем новую строку в нижнюю часть таблицы
            table.insertRow(row_position)

            # Заполняем ячейки новыми данными
            for index in range(6):
                item = QTableWidgetItem(data_row[index])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, index, item)

        #  Включаем сортировку
        table.setSortingEnabled(True)
