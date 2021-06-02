from Model.SimCard import SimCard


class PhoneNumber:
    """Класс номер телефона абонента"""
    def __init__(self, phone_number:str,simcard:SimCard):
        """Конструктор принимающий переменную phone_number
        phone_number [числовой] - номер телефона
        """
        self.phone_number = phone_number
        self.simcard = simcard

    def set_phone_number(self, phone_number:int):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    """set,get методы класса SimCard"""

    def set_SimCard(self, simcard: SimCard):
        self.simcard = simcard

    def get_SimCard(self):
        return self.simcard

    def __str__(self):
        return f"Номер телефона:{self.phone_number}"
