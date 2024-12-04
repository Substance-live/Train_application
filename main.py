import sys
from PySide6.QtWidgets import QApplication

#  Импорт форм окон
from layouts import (Ui_EditProfile, Ui_FastLogin, Ui_Login, Ui_MyTickets, Ui_Passenger, Ui_Profile, Ui_Railcar,
                     Ui_Registr, Ui_Ticket, Ui_mail_message)

#  Импорт вспомогательных классов
from static_methods import *


#  Импорт скрипта для обновления ui файлов (УДАЛИТЬ ПОЗЖЕ)
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
        self.engine = WindowsEngine(
            Ui_EditProfile,
            Ui_FastLogin,
            Ui_Login,
            Ui_MyTickets,
            Ui_Passenger,
            Ui_Profile,
            Ui_Railcar,
            Ui_Registr,
            Ui_Ticket,
            Ui_mail_message,
        )
        self.db = DataBase()
        self.user = User(self.db)
        self.current_ticket = Ticket()
        self.connect_widgets()

    def connect_widgets(self):
        """Назначает всем виджетам сигналы"""

        # Подключение для окна регистрации
        self.engine.get_widget("Registr", "but_login").clicked.connect(
            lambda: Show.login(
                self.engine,
            )
        )
        self.engine.get_widget("Registr", "check_confirm").stateChanged.connect(
            lambda: Check.confirm_registr(
                self.engine.get_widget("Registr", "but_registr"),
                self.engine.get_widget("Registr", "check_confirm")
            )
        )
        self.engine.get_widget("Registr", "but_registr").clicked.connect(
            lambda: (
                Data.registr(
                    self.engine,
                    self.db,
                    self.engine.get_widget("Registr", "entry_mail").text(),
                ),
                Show.login(
                    self.engine,
                )
            )
        )

        # Подключение для окна авторизации
        self.engine.get_widget("Login", "but_registr").clicked.connect(
            lambda: Show.registr(
                self.engine
            )
        )
        self.engine.get_widget("Login", "but_alter_login").clicked.connect(
            lambda: Show.alter_login(
                self.engine,
            )
        )
        self.engine.get_widget("Login", "but_login").clicked.connect(
            lambda: (
                Data.login(
                    self.engine,
                    self.db,
                    self.user,
                    self.engine.get_widget("Login", "entry_email").text(),
                    self.engine.get_widget("Login", "entry_passwd").text(),
                    self.current_ticket
                ),
            )
        )

        # Подключение для окна авторизации по почте
        self.engine.get_widget("FastLogin", "but_login").clicked.connect(
            lambda: Show.login(
                self.engine,
            )
        )
        self.engine.get_widget("FastLogin", "but_send_messenge").clicked.connect(
            lambda: QMessageBox.information(self.engine.windows['FastLogin'], "Авторизация",
                                    "На почту отправлен пароль для авторизации", QMessageBox.Ok)
        )
        self.engine.get_widget("FastLogin", "but_registr").clicked.connect(
            lambda: Show.registr(
                self.engine
            )
        )

        #  Подключения для окна профиля
        self.engine.get_widget("Profile", 'but_logout').clicked.connect(
            lambda: (
                Data.logout(
                    self.user,
                ),
                Show.login(
                    self.engine,
                )
            )
        )
        self.engine.get_widget("Profile", "but_edit").clicked.connect(
            lambda: Show.edit_profile(
                self.engine
            )
        )
        self.engine.get_widget("Profile", "but_orders").clicked.connect(
            lambda: Show.my_tickets(
                self.engine,
                self.db,
                self.user,
            )
        )
        self.engine.get_widget("Profile", "but_timetable").clicked.connect(
            lambda: Show.ticket(
                self.engine,
                self.db,
            )
        )

        #  Подключение для окна редактирования профиля
        self.engine.get_widget("EditProfile", "but_save").clicked.connect(
            lambda: (
                Data.edit_profile(
                    self.db,
                    self.user,
                    self.engine.get_widget("EditProfile", "entry_name").text(),
                    self.engine.get_widget("EditProfile", "entry_surname").text(),
                    self.engine.get_widget("EditProfile", "entry_patronymic").text(),
                    self.engine.get_widget("EditProfile", "entry_phone").text(),
                    self.engine.get_widget("EditProfile", "date_edit").date().toString("yyyy-MM-dd"),
                ),
                Show.profile(
                    self.engine,
                    self.current_ticket
                ),
            )
        )
        self.engine.get_widget("EditProfile", "check_confirm").stateChanged.connect(
            lambda: Check.confirm_registr(
                self.engine.get_widget("EditProfile", "but_save"),
                self.engine.get_widget("EditProfile", "check_confirm"))
        )
        self.engine.get_widget("EditProfile", "but_return").clicked.connect(
            lambda: Show.profile(
                self.engine,
                self.current_ticket,
            )
        )

        #  Подключение для окна просмотра истории билетов
        self.engine.get_widget("MyTickets", "but_return").clicked.connect(
            lambda: Show.profile(
                self.engine,
                self.current_ticket
            )
        )
        self.engine.get_widget("MyTickets", "but_refund").clicked.connect(
            lambda: (
                Data.cancel_ticket(self.engine, self.db),
                Show.my_tickets(
                    self.engine,
                    self.db,
                    self.user,
                )
            )
        )
        self.engine.get_widget("MyTickets", "but_del").clicked.connect(
            lambda: (
                Data.del_ticket(
                    self.engine,
                    self.db,
                ),
                Show.my_tickets(
                    self.engine,
                    self.db,
                    self.user,
                )
            )
        )

        #  Подключение для окна выбора билета
        self.engine.get_widget("Ticket", "combo_departure").lineEdit().textChanged.connect(
            lambda: Check.change(
                self.engine.get_widget("Ticket", "combo_departure"),
                self.engine.windows["Ticket"],
                "flag_dep",
                Data.get_stations(
                    self.db
                )
            )
        )
        self.engine.get_widget("Ticket", "combo_destination").lineEdit().textChanged.connect(
            lambda: Check.change(
                self.engine.get_widget("Ticket", "combo_destination"),
                self.engine.windows["Ticket"],
                "flag_arr",
                Data.get_stations(
                    self.db
                )
            )
        )
        self.engine.get_widget("Ticket", "but_search").clicked.connect(
            lambda: Data.reload_timtable(
                self.db,
                self.engine,
            )
        )
        self.engine.get_widget("Ticket", 'but_switch').clicked.connect(
            lambda: Data.switch_stations(
                self.engine,
            )
        )
        self.engine.get_widget("Ticket", "but_back").clicked.connect(
            lambda: Show.profile(
                self.engine,
                self.current_ticket
            )
        )
        self.engine.get_widget("Ticket", "but_confirm").clicked.connect(
            lambda: Show.railcar(
                self.engine,
                self.db,
                self.current_ticket,
            )
        )

        #  Подключение для окна вагонов
        self.engine.get_widget("Railcar", "but_back").clicked.connect(
            lambda: Show.ticket(
                self.engine,
                self.db,
            )
        )
        self.engine.get_widget("Railcar", "table_railcar").currentCellChanged.connect(
            lambda: Data.reload_price(
                self.db,
                self.engine
            )
        )
        self.engine.get_widget("Railcar", "spin_box_children").valueChanged.connect(
            lambda: Data.reload_price(
                self.db,
                self.engine
            )
        )
        self.engine.get_widget("Railcar", "spin_box_adult").valueChanged.connect(
            lambda: Data.reload_price(
                self.db,
                self.engine
            )
        )
        self.engine.get_widget("Railcar", "but_to_passenger").clicked.connect(
            lambda: Show.passenger(
                self.engine,
                self.db,
                self.current_ticket,
            )
        )
        #  Подключение для окна пассажиров
        self.engine.get_widget("Passenger", "but_back").clicked.connect(
            lambda: Show.railcar(
                self.engine,
                self.db,
                self.current_ticket
            )
        )
        self.engine.get_widget("Passenger", "but_buy").clicked.connect(
            lambda: (
                QMessageBox.information(self.engine.windows['Login'], "Покупка",
                                        "Билет успешно приобретён", QMessageBox.Ok),
                self.db.update_data(f"INSERT INTO `train`.`ticket` ("
                                    f"`idUser`, "
                                    f"`idRailcar`, "
                                    f"`idPassenger`, "
                                    f"`idStatus`, "
                                    f"`idFlight`) VALUES ({self.user.id}, "
                                    f"{self.current_ticket.railcar}, "
                                    f"1, "
                                    f"3, "
                                    f"{self.current_ticket.id});"),
                Show.profile(
                    self.engine,
                    self.current_ticket,
                ),

            )
        )
        self.engine.get_widget("Passenger", "combo_passenger").highlighted.connect(
            lambda: Check.save_data_passenger(self.engine.get_widget("Passenger", "combo_passenger"),
                                      self.engine.windows["Passenger"], self.current_ticket)
        )
        self.engine.get_widget("Passenger", "combo_passenger").currentIndexChanged.connect(
            lambda: Data.load_passenger(
                self.engine,
                self.current_ticket
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.engine.show_window("Login")
    sys.exit(app.exec())
