from Model.City import City


class Address:
    """Класс Адресс,где проживает абоненет """

    def __init__(self, street: str, home: str, city: City):
        """Конструктор принимающий переменные street,home
        street [строковый] - название улицы по которой проживает абонент
        home [числовой] - номер дома в котором проживает абонент
        """
        self.street = street
        self.home = home
        self.city = city

    def set_street(self, street: str):
        self.street = street

    def set_home(self, home: str):
        self.home = home

    def get_street(self):
        return self.street

    def get_home(self):
        return self.home

    """set,get методы класса City"""

    def set_city(self, city: City):
        self.city = city

    def get_city(self):
        return self.city

    def __str__(self):
        return f"Улица:{self.street} Дом:{self.home}"
