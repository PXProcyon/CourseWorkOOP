from Model.Abonent import Abonent

class Contract:
    """Класс Контракт """

    def __init__(self, date: str, number_contract: int, abonent: Abonent,
                 number_abonent: int, ):
        """Конструктур принимающий переменные date,number_contract,abonent,number_abonent,tarif,status
        date [строковый] - дата контракта
        number_contract [числовой] - номер абконтракта
        abonent [Класс Абонент] - ссылка на абонента
        number_abonent [числовой] - номер абонента

        """
        self.date = date
        self.number_contract = number_contract
        self.abonent = abonent
        self.number_abonent = number_abonent


    """set методы"""

    def set_date(self, date: str):
        self.date = date

    def set_number_contract(self, number_contract: int):
        self.number_contract = number_contract

    def set_number_abonent(self, number_abonent: int):
        self.number_abonent = number_abonent



        """get методы"""

    def get_date(self):
        return self.date

    def get_number_contract(self):
        return self.number_contractl

    def get_number_abonent(self):
        return self.number_abonent



        """set,get методы класса Abonent"""

    def set_abonent(self, abonent: str):
        self.abonent = abonent

    def get_abonent(self):
        return self.abonent

    def __str__(self):
        return f"Дата:{self.date} Номер контракта:{self.number_contract} Номер абонента:{self.number_abonent}"

