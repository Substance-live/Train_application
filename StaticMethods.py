from PySide6.QtWidgets import QPushButton, QCheckBox, QMessageBox

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


class Account:

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


