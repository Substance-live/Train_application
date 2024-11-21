#  Импорт библиотек
from datetime import date
from typing import Tuple

#  Импорт вспомогательных классов
from data_base import DataBase


class User:
    """Хранит информацию о залогиненном пользователе и обспечивает интерфейс входа и выхода из аккаунта

    АТРИБУТЫ:
    ---------
    __database  :   DataBase - Хранит ссылку на объект интерфейса работы с БД \n
    __personal_info    :   Dict - Словарь с персональной информацией о пользователе \n

    МЕТОДЫ:
    -------
    login(self, id_user: int) - Загружаем персональные данные из БД по id_user \n
    logout(self) - Устанавливает все персональные данные на None \n

    ПРИМЕЧАНИЕ:
    -----------

    ОШИБКИ:
    -------


    """

    def __init__(self, database: DataBase):
        """Создаём поля с персональными данными, базой данных и обнуляем на момент начала программы"""

        self.__database = database

        # Персональные данные
        self.__personal_info = dict()
        self.logout()  # Устанавливаем значения информации на по умолчанию

    def logout(self):
        """Устанавливает все персональные данные на None"""

        self.__personal_info = {
            "email": None,
            "name": None,
            "surname": None,
            "patronymic": None,
            "phone": None,
            "birthday": None,
        }

    def load_profile(self, id_user: int):
        """Загружаем персональные данные из БД по id_user"""

        data = self.__database.get_data(f"SELECT email, name, surname, patronymic, telephone, birthday "
                                        f"FROM user "
                                        f"WHERE idUser={id_user}", single_line=True)

        new_dict = dict()
        for index, attr in enumerate(self.__personal_info.keys()):
            new_dict[attr] = data[index]
        self.__personal_info = new_dict

    @property
    def personal_info(self) -> Tuple[str, ...]:
        return tuple(self.__personal_info[i] for i in self.__personal_info.keys())


if __name__ == '__main__':
    user = User(DataBase())
    user.load_profile(1)
    print(user.personal_info)
