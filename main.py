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
                Account.registr(
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
                Account.login(
                    self.engine,
                    self.db,
                    self.user,
                    self.engine.get_widget("Login", "entry_email").text(),
                    self.engine.get_widget("Login", "entry_passwd").text(),
                ),
                Show.profile(
                    self.engine,
                )
            )
        )

        # Подключение для окна авторизации по почте
        self.engine.get_widget("FastLogin", "but_login").clicked.connect(
            lambda: Show.login(
                self.engine,
            )
        )
        self.engine.get_widget("FastLogin", "but_registr").clicked.connect(
            lambda: Show.registr(
                self.engine
            )
        )
        self.engine.get_widget("FastLogin", "but_send_messenge").clicked.connect(
            lambda: Account.send_message(
                self.engine,
            )
        )

        #  Подключения для окна профиля
        self.engine.get_widget("Profile", 'but_logout').clicked.connect(
            lambda: (
                Account.logout(
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

        #  Подключение для окна редактирования профиля
        self.engine.get_widget("EditProfile", "but_save").clicked.connect(
            lambda: (
                Account.edit_profile(
                    self.db,
                    self.user,
                    self.engine.get_widget("EditProfile", "entry_name").text(),
                    self.engine.get_widget("EditProfile", "entry_surname").text(),
                    self.engine.get_widget("EditProfile", "entry_patronymic").text(),
                    self.engine.get_widget("EditProfile", "entry_phone").text(),
                    self.engine.get_widget("EditProfile", "date_edit").date().toString("yyyy-MM-dd"),
                ),
                Show.profile(
                    self.engine
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
            )
        )

        #  Подключение для окна просмотра истории билетов
        self.engine.get_widget("MyTickets", "but_return").clicked.connect(
            lambda: Show.profile(
                self.engine,
            )
        )
        self.engine.get_widget("MyTickets", "but_refund").clicked.connect(
            lambda: (
                Account.cancel_ticket(self.engine, self.db),
                Show.my_tickets(
                    self.engine,
                    self.db,
                    self.user,
                )
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.engine.show_window("Login")
    sys.exit(app.exec())
