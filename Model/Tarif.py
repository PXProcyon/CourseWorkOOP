from Model.Changelog import Changelog


class Tarif:
    """Класс тарифа абонента"""

    def __init__(self, anothet_minute: int, home_minute: int,
                 sms: int, internet: str, speed_internet: str, cost: str, transition_number: str,
                 changelog: Changelog):
        """
        anothet_minute [числовой] - Количество минут на номера других оператора
        home_minute [числовой] - Количество минут на номера домашнего оператора
        sms [числовой] - Количество смс
        internet [числовой] - Количество интернета-соединения
        speed_internet [числовой] - Скорость интернет-соединения
        cost [числовой] - Стоимость тарифа
        transition_number [числовой] - Номер перехода на тариф
        """
        self.anothet_minute = anothet_minute
        self.home_minute = home_minute
        self.sms = sms
        self.internet = internet
        self.speed_internet = speed_internet
        self.cost = cost
        self.transition_number = transition_number
        self.changelog = changelog

        """set методы"""

    def set_anothet_minute(self, anothet_minute: int):
        self.anothet_minute = anothet_minute

    def set_home_minute(self, home_minute: int):
        self.home_minute = home_minute

    def set_sms(self, sms: int):
        self.sms = sms

    def set_internet(self, internet: int):
        self.internet = internet

    def set_speed_internet(self, speed_internet: int):
        self.speed_internet = speed_internet

    def set_cost(self, cost: int):
        self.cost = cost

    def set_transition_number(self, transition_number: int):
        self.transition_number = transition_number

    """get методы"""

    def get_anothet_minute(self):
        return self.anothet_minute

    def get_home_minute(self):
        return self.home_minute

    def get_sms(self):
        return self.sms

    def get_internet(self):
        return self.internet

    def get_speed_internet(self):
        return self.speed_internet

    def get_cost(self):
        return self.cost

    def get_transition_number(self):
        return self.transition_number

    """set,get методы класса Changelog"""

    def set_changelog(self, changelog: Changelog):
        self.changelog = changelog

    def get_changelog(self):
        return self.changelog

    def __str__(self):
        return f"Количкество минут на номера других оператора:{self.anothet_minute} Количество минут на номера домашнего оператора:{self.home_minute}" \
               f" Количество смс:{self.sms} Количество интернета-соединения:{self.internet} " \
               f"Скорость интернет-соединения:{self.speed_internet} Стоимость тарифа:{self.cost} Номер перехода на тариф:{self.transition_number}"

