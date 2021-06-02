from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.ContractDialog import Ui_Dialog
from QT_view.ContractAdd import ContarctAddDialog
from Repository.Rep_Contract import ContractRepository



class ContractQt(QDialog):
    def __init__(self):
        super(ContractQt, self).__init__()
        self.contract_rep = ContractRepository()
        self.initUI()

    def initUI(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(1, 259)
        self.ui.tableWidget.setSelectionBehavior(1)
        self.ui.tableWidget.setSelectionMode(1)

        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.pushButton_2.clicked.connect(self.click_edit)
        self.ui.pushButton_3.clicked.connect(self.click_del)
        self.ui.pushButton_4.clicked.connect(self.click_cancel)

        contract = self.contract_rep.get_contracts()
        self.ui.tableWidget.setRowCount(len(contract))
        row = 0
        for i in contract:
            id_contract = QTableWidgetItem(str(i['id']))
            id_contract.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            date = QTableWidgetItem(i['date'])
            date.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            number_contract = QTableWidgetItem(str(i['number_contract']))
            number_contract.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            number_abonent = QTableWidgetItem(str(i['number_abonent']))
            number_abonent.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_contract)
            self.ui.tableWidget.setItem(row, 1, date)
            self.ui.tableWidget.setItem(row, 2, number_contract)
            self.ui.tableWidget.setItem(row, 3, number_abonent)
            row += 1

    def click_add(self):
        p_dict = {'id': -1,'date': "", 'number_contract': "", 'number_abonent': ""}
        self.contract_rep.set_dict(p_dict)
        contract_add = ContarctAddDialog(self.contract_rep)
        if (contract_add.exec()):
            contract_d = self.contract_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            date = QTableWidgetItem(contract_d['date'])
            date.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            number_contract = QTableWidgetItem(contract_d['number_oontract'])
            number_contract.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            number_abonent = QTableWidgetItem(contract_d['number_abonent'])
            number_abonent.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, date)
            self.ui.tableWidget.setItem(count_row, 2, number_contract)
            self.ui.tableWidget.setItem(count_row, 3, number_abonent)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()),'date': edit_list[1].text(),'number_contract': edit_list[2].text(),'number_abonent': edit_list[3].text()}
            self.contract_rep.set_dict(edit_d)
            contract_edit = ContarctAddDialog(self.contract_rep)
            if (contract_edit.exec()):
                contract_d = self.contract_rep.get_dict()

                date = QTableWidgetItem(contract_d['date'])
                date.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                number_contract = QTableWidgetItem(contract_d['number_contract'])
                number_contract.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                number_abonent = QTableWidgetItem(contract_d['number_abonent'])
                number_abonent.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, date)
                self.ui.tableWidget.setItem(select_row, 2, number_contract)
                self.ui.tableWidget.setItem(select_row, 3, number_abonent)
    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_con = {'id': int(del_list[0].text()),'date': del_list[1].text(), 'number_contract': del_list[2].text(),
                       'number_abonent': del_list[3].text()}
            self.contract_rep.del_contract(del_con)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()