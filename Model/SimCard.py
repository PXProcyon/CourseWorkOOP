from Model.Contract import Contract



class SimCard:
    """Класс сим-карты абонента"""
    def __init__(self,ICCIM:int,contract:Contract):
        """Конструктор принимающий переменную ,ICCIM
        ICCIM [числовой] - уникальный серийный номер сим-карты
        """
        self.ICCIM = ICCIM
        self.contract = contract

    def set_ICCIM(self, ICCIM: str):
        self.ICCIM = ICCIM

    def get_ICCIM(self):
        return self.ICCIM

    """set,get методы класса Contract"""

    def set_contract(self, contract : str):
        self.contract = contract

    def get_contract(self):
        return self.contract

    def __str__(self):
        return f"Номер ICCIM:{self.ICCIM}"

