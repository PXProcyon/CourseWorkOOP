from Model.Contract import Contract


class PersonalAccount:
    """Класс лицевой счёт абонетна"""

    def __init__(self, current_balance: int, deposit_history: str, history_writedowns: str, contract: Contract):
        """Конструктор принимающий переменные current_balance,deposit_history,history_writedowns
        current_balance [числовой] - текущий счёт абонента
        deposit_history [строковый] - история пополнения баланса абонента
        history_writedowns [строковый] - история списания баланса абонента
        """
        self.current_balance = current_balance
        self.deposit_history = deposit_history
        self.history_writedowns = history_writedowns
        self.contract = contract

        def set_current_balance(self, current_balance: int):
            self.current_balance = current_balance

        def set_deposit_history(self, deposit_history: str):
            self.deposit_history = deposit_history

        def set_history_writedowns(self, history_writedowns: str):
            self.history_writedowns = history_writedowns

        def get_current_balance(self):
            return self.current_balance

        def get_deposit_history(self):
            return self.deposit_history

        def get_history_writedowns(self):
            return self.hhistory_writedowns

        """set,get методы класса Contract"""

        def set_contract(self, contract: Contract):
            self.contract = contract

        def get_contarct(self):
            return self.contaract
