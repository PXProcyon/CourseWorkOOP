from Model.Adress import Address
from Model.Passport import Passport


class Abonent:
    """Класс Абонент,человек желающий подключить к мобильному устройству тариф """

    def __init__(self, subname: str, name: str, patronymic: str, age: int, passport: Passport, address: Address):
        """Конструктор принимающий переменные subname,name,patronymic,age
        subname [строковый] - фамилия абонента
        name [строковый] - имя абонента
        patronymic [строковый] - отчество абонента
        age [числовой] - возраст абонента
        """
        self.subname = subname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.passport = passport
        self.address = address

        """set методы"""

    def set_subname(self, subname: str):
        self.subname = subname

    def set_name(self, name: str):
        self.name = name

    def set_patronymic(self, patronymic: str):
        self.patronymic = patronymic

    def set_age(self, age: int):
        self.age = age

    """get методы"""

    def get_subname(self):
        return self.subname

    def get_name(self):
        return self.name

    def get_patronymic(self):
        return self.patronymic

    def get_age(self):
        return self.age

    """set,get методы класса Passport"""

    def set_passport(self, passport: Passport):
        self.passport = passport

    def get_passport(self):
        return self.passport

    """set,get методы класса Address"""

    def set_address(self, address: Address):
        self.address = address

    def get_address(self):
        return self.address

    def __str__(self):
        return f"Фамилия:{self.subname} Имя:{self.name} Отчество:{self.patronymic}"