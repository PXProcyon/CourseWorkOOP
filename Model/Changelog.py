from Model.PhoneNumber import PhoneNumber


class Changelog:
    """Класс история изменения тарифа"""
    def __init__(self,data_change:str,content:str,phonenumber:PhoneNumber):
        """Конструктор принимающий переменные data_change,contect
        data_change [строковый] - Дата изменения тарифа
        contect [строковый] - содержание изменения тарифа
        """
        self.date_change = data_change
        self.content = content
        self.phonenumber = phonenumber

    def set_data_change(self, data_change:str):
        self.data_change = data_change

    def set_content(self, content:str):
        self.content = content

    def get_data_change(self):
        return self.data_change

    def get_content(self):
        return self.content

    """set,get методы класса PhoneNumber"""

    def set_phone_number(self, phone_number: PhoneNumber):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def __str__(self):
        return f"Дата изменения:{self.date_change} Содержание изменения:{self.content}"