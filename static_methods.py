import datetime
import os

from PySide6.QtWidgets import (QPushButton, QCheckBox, QMessageBox, QTableWidget, QTableWidgetItem, QComboBox,
                               QDateEdit, QLabel, QSpinBox, QFileDialog)
from PySide6.QtCore import Qt, QDate

#  Импорт вспомогательных классов
from windows import WindowsEngine
from data_base import DataBase
from user import User
from ticket import Ticket


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

    @staticmethod
    def save_data_passenger(combo_box: QComboBox, window, ticket: Ticket):
        surname: str = window.line_surname.text()
        name: str = window.line_name.text()
        patronymic: str = window.line_patronymic.text()
        gender_m: str = window.radio_male.isChecked()
        gender_f: str = window.radio_female.isChecked()
        birthday: str = window.date_birthday.date()
        id_doc: int = window.combo_document.currentIndex()
        number_doc: str = window.line_num_document.text()

        print(combo_box.currentIndex(), ticket.people)
        ticket.people[combo_box.currentIndex()] = [surname, name, patronymic, gender_m, gender_f, birthday, id_doc,
                                                   number_doc]

        print(ticket.people)


class Show:

    @staticmethod
    def admin_flight(engine: WindowsEngine, db: DataBase):
        #  Загружаем данные из бд и подготавливаем переменную с таблицей
        data = Data.load_admin_flight(db)
        table: QTableWidget = engine.get_widget("AdminTickets", "table_timetable")

        engine.show_window("AdminTickets")

        #  Отключаем сортировку
        table.setSortingEnabled(False)
        table.blockSignals(True)

        for data_row in data:
            row_position = table.rowCount()

            # Вставляем новую строку в нижнюю часть таблицы
            table.insertRow(row_position)

            # Заполняем ячейки новыми данными
            for index in range(7):
                item = QTableWidgetItem(data_row[index])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, index, item)

        #  Включаем сортировку
        table.setSortingEnabled(True)
        table.blockSignals(False)

    @staticmethod
    def admin_users(engine: WindowsEngine, db: DataBase):

        #  Загружаем данные из бд и подготавливаем переменную с таблицей
        data = Data.load_admin_users(db)
        table: QTableWidget = engine.get_widget("AdminUsers", "table")

        engine.show_window("AdminUsers")

        #  Отключаем сортировку
        table.setSortingEnabled(False)
        table.blockSignals(True)

        for data_row in data:
            row_position = table.rowCount()

            # Вставляем новую строку в нижнюю часть таблицы
            table.insertRow(row_position)

            # Заполняем ячейки новыми данными
            for index in range(8):
                item = QTableWidgetItem(data_row[index])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, index, item)

        #  Включаем сортировку
        table.setSortingEnabled(True)
        table.blockSignals(False)

    @staticmethod
    def admin_profile(engine: WindowsEngine):
        engine.show_window("AdminProfile")

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
    def profile(engine: WindowsEngine, ticket: Ticket):
        ticket.reset_values()
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
            for index in range(7):
                item = QTableWidgetItem(data_row[index])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, index, item)

        #  Включаем сортировку
        table.setSortingEnabled(True)

    @staticmethod
    def railcar(engine: WindowsEngine, db: DataBase, ticket: Ticket):
        table_last: QTableWidget = engine.get_widget("Ticket", "table_timetable")
        table: QTableWidget = engine.get_widget("Railcar", "table_railcar")

        row = table_last.item(table_last.currentRow(), 0)
        if not (row is None):
            ticket.id = int(row.text()) - 735130

        item = ticket.id

        ticket.railcar = -1

        data = Data.loar_railcars(db, item)

        engine.get_widget("Railcar", "label_price").setText("0$")

        engine.show_window("Railcar")

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
    def passenger(engine: WindowsEngine, db: DataBase, ticket: Ticket):
        last_price: QLabel = engine.get_widget("Railcar", "label_price")
        last_table: QTableWidget = engine.get_widget("Railcar", "table_railcar")
        last_spin_child: QSpinBox = engine.get_widget("Railcar", "spin_box_children")
        last_spin_adult: QSpinBox = engine.get_widget("Railcar", "spin_box_adult")

        id_railcar = int(last_table.item(last_table.currentRow(), 0).text())
        price = int(last_price.text()[:-1])
        count_passenger = int(last_spin_adult.value()) + int(last_spin_child.value())
        type = last_table.item(last_table.currentRow(), 3).text()
        bizness_class = last_table.item(last_table.currentRow(), 2).text()

        ticket.type = type
        ticket.bizness_class = bizness_class
        ticket.railcar = id_railcar
        ticket.price = price
        ticket.count_passenger = count_passenger
        ticket.people = [['', '', '', False, False, QDate(2000, 1, 1), -1, ''] for i in range(ticket.count_passenger)]

        label: QLabel = engine.get_widget("Passenger", "label_price")
        combo_passenger: QComboBox = engine.get_widget("Passenger", "combo_passenger")

        engine.show_window("Passenger")

        label.setText(f"{price}$")
        combo_passenger.addItems([f"Пассажир {i}" for i in range(1, count_passenger + 1)])


class Data:

    @staticmethod
    def save_file(engine: WindowsEngine, db: DataBase):
        from docxtpl import DocxTemplate
        from docx2pdf import convert

        options = QFileDialog.Options()
        file_name = QFileDialog.getSaveFileName(
            engine.windows["MyTickets"],
            "Сохранить файл как",
            "",
            "PDF Files (*.pdf);;All Files (*)",
            options=options
        )

        table = engine.get_widget("MyTickets", "table")
        id_ticket = int(table.item(table.currentRow(), 0).text()) - 735130
        doc = DocxTemplate("data/blueprint/blueprint_train.docx")
        data_1 = db.get_data(
            "SELECT t.idTicket, concat(p.surname, ' ', left(p.name, 1), '. ', left(p.patronymic, 1), '.'), td.title, "
            "d.number, r.type, r.class_of_service, r.idRailcar, t.count "
            "FROM ticket as t "
            "JOIN passenger as p ON p.idPassenger=t.idPassenger "
            "JOIN document as d ON d.idDocument=p.idDocument "
            "JOIN type_document as td ON td.idTypeDocument=d.idTypeDocument "
            "JOIN railcar as r ON r.idRailcar=t.idRailcar "
            f"WHERE t.idTicket = {id_ticket}", single_line=True)

        print(id_ticket, db.get_data(f"select idFlight from ticket where idTicket={id_ticket}", single_line=True))
        data_2 = [i for i in db.get_data("call tickets_common()")
                  if i[0] == db.get_data(f"select idFlight from ticket where idTicket={id_ticket}", single_line=True)[0]
                  ][0]
        print(data_1, data_2)
        context = {
            "train": 'Сапсан',  # const
            "nds": '20',  # const
            "current_date": datetime.datetime.today().strftime("%Y-%m-%d"),  # Текущая дата

            "id_ticket": f'{data_1[0] + 735130}',  # 735130 + id, где * - Id маршрута вкладки ticket
            "fio": f'{data_1[1]}',  # Фио вкладки passenger
            "document_title": f'{data_1[2]}',  # Тип документа во вкладке passenger
            "document_id": f'{data_1[3]}',  # Номер документа во вкладке passenger
            "type": f'{data_1[4]}',  # Тип вагона railcar
            "class": f'{data_1[5]}',  # Класс обсуживания railcar

            "date": f'{data_2[3].strftime("%d.%m.%Y")}',  # Дата выбранного маршрута вкладки ticket
            "departure": f'{data_2[1]}',  # Поле отправки вкладки ticket
            "arrival": f'{data_2[2]}',  # Поле прибытия вкладки ticket
            "departure_time": f'{data_2[3].strftime("%H:%M")}',  # Время отправки ticket
            "arrival_time": f'{data_2[3].strftime("%H:%M")}',  # Время прибытия ticket
            "railcar": f'{data_1[-2]}',

            "price_ticket": f'{data_1[-1] * data_2[-2]}',  # Цена из вкладки railcar
            "nds_price_ticket": f'{(float(data_1[-1] * data_2[-2]) * 1.2):.1f}',  # price_ticket * nds%


        }
        path = f"data/blueprint/{file_name[0].split('/')[-1][:-4]}.docx"
        doc.render(context)
        doc.save(path)
        convert(path, file_name[0])
        os.remove(path)

    @staticmethod
    def but_ticket(engine: WindowsEngine, db: DataBase, user: User, current_ticket: Ticket):
        window = engine.windows["Passenger"]
        db.update_data(
            f"INSERT INTO document ("
            f"idTypeDocument, number) VALUES"
            f"({window.combo_document.currentIndex() + 1}, {window.line_num_document.text()});"
        )
        db.update_data(
            f"INSERT INTO passenger ("
            f"idDocument, name, surname, patronymic, gender, birthday) VALUES ("
            f"{db.get_data("SELECT * FROM document")[-1][0]},"
            f"'{window.line_name.text()}',"
            f"'{window.line_surname.text()}',"
            f"'{window.line_patronymic.text()}',"
            f"'*',"
            f"'*');"
        )
        db.update_data(
            f"INSERT INTO `train`.`ticket` ("
            f"`idUser`, "
            f"`idRailcar`, "
            f"`idPassenger`, "
            f"`idStatus`, "
            f"`idFlight`, "
            f"`count`) VALUES ("
            f"{user.id}, "
            f"{current_ticket.railcar}, "
            f"{db.get_data("SELECT * FROM passenger")[-1][0]}, "
            f"3, "
            f"{current_ticket.id},"
            f"{current_ticket.count_passenger});"),

    @staticmethod
    def edit_cell(row, engine: WindowsEngine, db: DataBase):
        table = engine.get_widget("AdminUsers", "table")
        id_user = table.item(row, 0).text()
        ret = []
        for i in range(1, table.columnCount()):
            ret.append(table.item(row, i).text())
        db.update_data(
            "UPDATE `train`.`user` SET "
            f"`email` = '{ret[0]}',"
            f"`password` = '{ret[1]}',"
            f"`name` = '{ret[2]}',"
            f"`surname` = '{ret[3]}',"
            f"`patronymic` = '{ret[4]}',"
            f"`phone` = '{ret[5]}',"
            f"`birthday` = '{ret[6]}'"
            f"WHERE `idUser` = '{id_user}';")

    @staticmethod
    def add_row(engine: WindowsEngine, db: DataBase):
        db.update_data(
            "INSERT INTO `train`.`user`"
            "(`email`,`password`,`name`,`surname`,`patronymic`,`phone`,`birthday`)"
            'VALUES ("", "", "", "", "", "", "2020-01-01");'
        )
        QMessageBox.information(engine.windows['AdminUsers'], "Пустой пользователь добавлен",
                                "Пользователь успешно добавлен", QMessageBox.Ok)

    @staticmethod
    def delete_row_flight(engine: WindowsEngine):
        table = engine.get_widget("AdminTickets", "table_timetable")
        table.removeRow(table.currentRow())

    @staticmethod
    def add_row_flight(engine: WindowsEngine):
        table = engine.get_widget("AdminTickets", "table_timetable")
        row_position = table.rowCount()

        # Вставляем новую строку в нижнюю часть таблицы
        table.insertRow(row_position)

    @staticmethod
    def delete_row(engine: WindowsEngine, db: DataBase):
        table = engine.get_widget("AdminUsers", "table")
        id_deleted_row = table.item(table.currentRow(), 0).text()
        db.update_data(
            "DELETE FROM `train`.`ticket`"
            f"WHERE `idUser` = '{id_deleted_row}';")
        db.update_data(
            "DELETE FROM `train`.`user` "
            f"WHERE `idUser` = '{id_deleted_row}';"
        )
        QMessageBox.information(engine.windows['AdminUsers'], "Пользователь удалён",
                                "Пользователь успешно удален", QMessageBox.Ok)

    @staticmethod
    def logout(user: User):
        user.logout()

    @staticmethod
    def login(engine: WindowsEngine, db: DataBase, user: User, email: str, password: str, ticket: Ticket):

        id_admin = db.get_data(
            "SELECT `idAdmin` "
            "FROM `admin` "
            f"WHERE `email`='{email}' AND `password`='{password}'", single_line=True)

        if not (id_admin is None):
            QMessageBox.information(engine.windows['Login'], "Успешная авторизации администратора",
                                    "Администратор успешно авторизирован", QMessageBox.Ok)
            Show.admin_profile(engine)
            return

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
        Show.profile(engine, ticket)

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
    def load_admin_flight(db: DataBase) -> list[list[str]]:
        data = db.get_data(
            "call tickets_common()"
        )
        print(data)
        ret = []
        for i in data:
            ret.append(
                [str(i[0]), i[1], i[2], i[3].strftime("%Y-%m-%d"), i[4].strftime("%Y-%m-%d"), str(i[5]), str(i[6])])

        print(ret)

        return ret

    @staticmethod
    def load_admin_users(db: DataBase) -> list[list[str]]:
        data = db.get_data(
            "SELECT * FROM `user`"
        )
        print(data)
        ret = []
        for i in data:
            ret.append(list(i))
            ret[-1][0] = str(ret[-1][0])
            ret[-1][7] = ret[-1][7].strftime("%Y-%m-%d")

        return ret

    @staticmethod
    def load_history(db: DataBase, user: User) -> list[list[str]]:
        data = db.get_data(
            "SELECT t.`idTicket`, f.`title`, tt.`departure`, r.`price`, s.`title`, t.`count`"
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
            ret.append([str(735130 + i[0]), i[1], i[2].strftime("%Y-%m-%d"), str(i[3] * i[5]), i[4]])

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
            print(args, "example")
            data = db.get_data(
                f"call tickets_extended('{args[0].split()[0]}', '{args[1].split()[0]}', '{args[2].split('.')[2]}-{args[2].split('.')[1]}-{args[2].split('.')[0]}')"
            )

        ret = []
        for i in data:
            ret.append([str(735130 + i[0]), i[1], i[2], i[3].strftime("%H:%M"),
                        i[4].strftime("%H:%M"), str(int(i[5])), str(i[6])])

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
                for index in range(7):
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
            for index in range(7):
                item = QTableWidgetItem(data_row[index])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row_position, index, item)

        #  Включаем сортировку
        table.setSortingEnabled(True)

    @staticmethod
    def switch_stations(engine: WindowsEngine):
        combo_dep: QComboBox = engine.get_widget("Ticket", "combo_departure")
        combo_arr: QComboBox = engine.get_widget("Ticket", "combo_destination")

        text_dep = combo_dep.lineEdit().text()
        text_arr = combo_arr.lineEdit().text()

        text_arr, text_dep = text_dep, text_arr

        combo_arr.lineEdit().setText(text_arr)
        combo_dep.lineEdit().setText(text_dep)

    @staticmethod
    def loar_railcars(db: DataBase, id_flight: int) -> list[list[str]]:
        data = db.get_data(f"call railcar_table({id_flight})")

        ret = []
        for i in data:
            ret.append([str(i[0]), str(i[1]), i[2], i[3], str(i[4])])

        return ret

    @staticmethod
    def reload_price(db: DataBase, engine: WindowsEngine):
        label: QLabel = engine.get_widget("Railcar", "label_price")
        spin_child: QSpinBox = engine.get_widget("Railcar", "spin_box_children")
        spin_adult: QSpinBox = engine.get_widget("Railcar", "spin_box_adult")
        table: QTableWidget = engine.get_widget("Railcar", "table_railcar")

        selected_row = table.item(table.currentRow(), 4)
        if selected_row is None:
            return
        price = int(selected_row.text())

        ret = (spin_adult.value() + spin_child.value()) * price
        label.setText(f"{ret}$")

    @staticmethod
    def load_passenger(engine: WindowsEngine, ticket: Ticket):
        window = engine.windows["Passenger"]
        index: int = engine.get_widget("Passenger", "combo_passenger").currentIndex()

        print("index", index)

        if index == -1:
            return

        lst = ticket.people[index]

        engine.get_widget("Passenger", "combo_document").clear()
        engine.get_widget("Passenger", "combo_document").addItems(["Паспорт",
                                                                   "Военный билет", "Лицензированный документ"])

        window.line_surname.setText(lst[0])
        window.line_name.setText(lst[1])
        window.line_patronymic.setText(lst[2])
        window.radio_male.setChecked(lst[3])
        window.radio_female.setChecked(lst[4])
        window.date_birthday.setDate(lst[5])
        window.combo_document.setCurrentIndex(lst[6])
        window.line_num_document.setText(lst[7])
