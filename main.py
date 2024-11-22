import sys
from PySide6.QtWidgets import QApplication, QPushButton, QCheckBox, QVBoxLayout, QMessageBox

#  Импорт форм окон
from layouts import (Ui_EditProfile, Ui_FastLogin, Ui_Login, Ui_MyTickets, Ui_Passenger, Ui_Profile, Ui_Railcar,
                     Ui_Registr, Ui_Ticket, Ui_mail_message)

#  Импорт вспомогательных классов
from windows import WindowsEngine
from data_base import DataBase
from user import User


#  Импорт скрипта для обновления ui файлов (УДАЛИТЬ ПОЗЖЕ)
# import convet_ui_files


def get_rand_passwd() -> str:
    return "random_password"


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
                self.engine.get_widget("Registr", "check_confirm"),
            )
        )
        self.engine.get_widget("Registr", "but_registr").clicked.connect(
            lambda: Account.registr(
                self.engine,
                self.db,
                self.engine.get_widget("Registr", "entry_mail").text(),
            )
        )

        # Подключение для окна авторизации
        self.engine.get_widget("Login", "but_registr").clicked.connect(
            lambda: Show.registr(
                self.engine,
                self.engine.get_widget("Registr", "but_registr"),
            )
        )
        self.engine.get_widget("Login", "but_alter_login").clicked.connect(
            lambda: Show.alter_login(
                self.engine,
            )
        )
        self.engine.get_widget("Login", "but_login").clicked.connect(
            lambda: Account.login(
                self.engine,
                self.db,
                self.user,
                self.engine.get_widget("Login", "entry_email").text(),
                self.engine.get_widget("Login", "entry_passwd").text(),
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
                self.engine,
                self.engine.get_widget("Registr", "but_registr"),
            )
        )
        self.engine.get_widget("FastLogin", "but_send_messenge").clicked.connect(
            lambda: Account.send_message(
                self.engine,
            )
        )

        #  Подключения для окна профиля
        self.engine.get_widget("Profile", 'but_logout').clicked.connect(
            lambda: Account.logout(
                self.engine,
                self.user,
            )
        )
        self.engine.get_widget("Profile", "but_edit").clicked.connect(
            lambda: Show.edit_profile(
                self.engine
            )
        )

        #  Подключение для окна редактирования профиля
        self.engine.get_widget("EditProfile", "but_save").clicked.connect(
            lambda: Account.edit_profile(
                self.db,
                self.user,
                self.engine.get_widget("EditProfile", "entry_name").text(),
                self.engine.get_widget("EditProfile", "entry_surname").text(),
                self.engine.get_widget("EditProfile", "entry_patronymic").text(),
                self.engine.get_widget("EditProfile", "entry_phone").text(),
                self.engine.get_widget("EditProfile", "date_edit").date().toString("yyyy-MM-dd"),
            )
        )


class Check:

    @staticmethod
    def confirm_registr(but_registr: QPushButton, check_confirm: QCheckBox):

        if check_confirm.isChecked():
            but_registr.setEnabled(True)
        else:
            but_registr.setEnabled(False)


class Show:

    @staticmethod
    def alter_login(engine: WindowsEngine):
        engine.show_window("FastLogin")

    @staticmethod
    def login(engine: WindowsEngine):
        engine.show_window("Login")

    @staticmethod
    def registr(engine: WindowsEngine, but_registr: QPushButton):
        engine.show_window("Registr")

        #  Блокируем кнопку регистрации до подтверждение обработки данных
        but_registr.setEnabled(False)

    @staticmethod
    def profile(engine: WindowsEngine):
        engine.show_window("Profile")

    @staticmethod
    def edit_profile(engine: WindowsEngine):
        engine.show_window("EditProfile")


class Account:

    @staticmethod
    def logout(engine: WindowsEngine, user: User):
        user.logout()
        Show.login(engine)

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
    def edit_profile(db: DataBase, user: User, name: str, surname: str, patronymic: str, phone: str, birthday: str):
        db.update_data(f"UPDATE `train`.`user` "
                       f"SET `name` = '{name}',"
                       f"`surname` = '{surname}',"
                       f"`patronymic` = '{patronymic}',"
                       f"`phone` = '{phone}',"
                       f"`birthday` = '{birthday}' "
                       f"WHERE `idUser` = {user.id};")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.engine.show_window("Login")
    sys.exit(app.exec())
