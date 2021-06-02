from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.AddressAdd import AddressAddDialog
from QT_view.AdressDialog import Ui_Dialog
from Repository.Rep_Address import AddressRepository

class AddressQt(QDialog):
    def __init__(self):
        super(AddressQt, self).__init__()
        self.address_rep = AddressRepository()
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

        address = self.address_rep.get_addresss()
        self.ui.tableWidget.setRowCount(len(address))
        row = 0
        for i in address:
            id_abonent = QTableWidgetItem(str(i['id']))
            id_abonent.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            street = QTableWidgetItem(i['street'])
            street.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            home = QTableWidgetItem(i['home'])
            home.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_abonent)
            self.ui.tableWidget.setItem(row, 1, street)
            self.ui.tableWidget.setItem(row, 2, home)
            row += 1

    def click_add(self):
        p_dict = {'id': -1,'street': "", 'home': ""}
        self.address_rep.set_dict(p_dict)
        address_add = AddressAddDialog(self.address_rep)
        if (address_add.exec()):
            address_d = self.address_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            street = QTableWidgetItem(address_d['street'])
            street.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            home = QTableWidgetItem(address_d['home'])
            home.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, street)
            self.ui.tableWidget.setItem(count_row, 2, home)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()),'street': edit_list[1].text(),'home': edit_list[2].text()}
            self.address_rep.set_dict(edit_d)
            address_edit = AddressAddDialog(self.address_rep)
            if (address_edit.exec()):
                address_d = self.address_rep.get_dict()
                street = QTableWidgetItem(address_d['street'])
                street.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                home = QTableWidgetItem(address_d['home'])
                home.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, street)
                self.ui.tableWidget.setItem(select_row, 2, home)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_a = {'id': int(del_list[0].text()), 'street': del_list[1].text(), 'home': del_list[2].text()}
            self.ui.tableWidget.removeRow(del_list[0].row())
            self.address_rep.del_address(del_a)

    def click_cancel(self):
        self.accept()