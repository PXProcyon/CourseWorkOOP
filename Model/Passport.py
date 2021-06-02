class Passport:
    """Класс Паспорт """

    def __init__(self, serial: str, number: str):
        """Конструктор принимающий переменные serial,number
        serial [строковый] - серия паспорта
        number [строковый] - номер паспорта
        """
        self.serial = serial
        self.number = number

    def set_serial(self, serial: str):
        self.serial = serial

    def set_number(self, number: str):
        self.number = number

    def get_serial(self):
        return self.serial

    def get_number(self):
        return self.number

    def __str__(self):
        return f"серия:{self.serial} номер:{self.number}"