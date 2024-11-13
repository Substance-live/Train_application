#  Импорт библиотек
from datetime import date

#  Импорт вспомогательных классов
from data_base import DataBase


class User:
    """

    АТРИБУТЫ:
    ---------

    МЕТОДЫ:
    -------

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------


    """

    def __init__(self, database: DataBase):
        """"""

        self.__database = database

        # Персональные данные
        self.__personal_info = dict()
        self.logout()  #  Устанавливаем значения информации на по умолчанию

    def logout(self):
        """"""

        self.__personal_info = {
            "email": None,
            "name": None,
            "surname": None,
            "patronymic": None,
            "phone": None,
            "birthday": None,
        }

    def login(self, id_user: int):
        """"""

        data = self.__database.get_data(f"SELECT email, name, surname, patronymic, telephone, birthday "
                                        f"FROM user "
                                        f"WHERE idUser={id_user}", single_line=True)

        new_dict = dict()
        for index, attr in enumerate(self.__personal_info.keys()):
            new_dict[attr] = data[index]
        self.__personal_info = new_dict

    @property
    def personal_info(self) -> dict[str: Any]:
        return self.__personal_info


if __name__ == '__main__':
    user = User(DataBase())
    user.login(1)
    print(user.personal_info)
