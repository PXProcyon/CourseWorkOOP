from PyQt5.QtWidgets import QDialog

from Repository.Rep_Contract import ContractRepository

from QT_view.ContractAddWin import Ui_Contract

class ContarctAddDialog(QDialog):
    def __init__(self,contract_rep: ContractRepository):
        super(ContarctAddDialog, self).__init__()
        self.contract_rep = contract_rep
        self.contract_d = contract_rep.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Contract()
        self.ui.setupUi(self)
        if (len(self.contract_d['date'])):
            self.ui.lineEdit_date.setText(self.contract_d['date'])

        if (len(self.contract_d['number_contract'])):
            self.ui.lineEdit_number_contract.setText(self.contract_d['number_contract'])

        if (len(self.contract_d['number_abonent'])):
            self.ui.lineEdit_number_abonent.setText(self.contract_d['number_abonent'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        co_date = self.ui.lineEdit_date.text()
        co_date = co_date.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        co_num_contract = self.ui.lineEdit_number_contract.text()
        co_num_contract = co_num_contract.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        co_num_abonent = self.ui.lineEdit_number_abonent.text()
        co_num_abonent = co_num_abonent.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.contract_d['id'] == -1):
            if (len(co_num_abonent)):
                self.contract_d['date'] = co_date
                self.contract_d['number_contract'] = co_num_contract
                self.contract_d['number_abonent'] = co_num_abonent
                self.contract_d['id'] = self.contract_rep.new_contract(self.contract_d)
                self.contract_rep.set_dict(self.contract_d)
                self.accept()
        else:
            if (len(co_num_abonent)):
                self.contract_d['date'] = co_date
                self.contract_d['number_contract'] = co_num_contract
                self.contract_d['number_abonent'] = co_num_abonent
                self.contract_rep.update_contract(self.contract_d)
                self.contract_rep.set_dict(self.contract_d)
                self.accept()
    def click_cancel(self):
        self.reject()