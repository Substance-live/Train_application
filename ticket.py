

class Ticket:

    def __init__(self):
        self.__id: int = -1
        self.__railcar: int = -1
        self.__price: int = -1
        self.__count_passenger: int = -1

    def __str__(self):
        return f"(idFlight={self.__id}, idRailcar={self.__railcar}, price={self.__price})"

    def reset_values(self):
        for attr in self.__dict__.keys():
            self.__dict__[attr] = -1

    @property
    def id(self):
        return self.__id

    @property
    def railcar(self):
        return self.__railcar

    @property
    def price(self):
        return self.__price

    @property
    def count_passenger(self):
        return self.__count_passenger

    @count_passenger.setter
    def count_passenger(self, value):
        self.__count_passenger = value

    @price.setter
    def price(self, value):
        self.__price = value

    @id.setter
    def id(self, value):
        self.__id = value

    @railcar.setter
    def railcar(self, value):
        self.__railcar = value


if __name__ == '__main__':
    a1 = Ticket()
    a1.price = 21
    print(a1)
    a1.reset_values()
    print(a1)