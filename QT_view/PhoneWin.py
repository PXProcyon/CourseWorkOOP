from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.PhoneDialog import Ui_Dialog
from QT_view.PhoneAdd import PhoneAddDialog
from Repository.Rep_PhoneNumber import PhoneNumberRepository


class PhoneQt(QDialog):
    def __init__(self):
        super(PhoneQt, self).__init__()
        self.phone_rep = PhoneNumberRepository()
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

        phone_number = self.phone_rep.get_phonenumbers()
        self.ui.tableWidget.setRowCount(len(phone_number))
        row = 0
        for i in phone_number:
            id_phonenumber = QTableWidgetItem(str(i['id']))
            id_phonenumber.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            phonenumber = QTableWidgetItem(str(i['phone_number']))
            phonenumber.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_phonenumber)
            self.ui.tableWidget.setItem(row, 1, phonenumber)
            row += 1

    def click_add(self):
        p_dict = {'id': -1, 'phone_number': ""}
        self.phone_rep.set_dict(p_dict)
        phone_add = PhoneAddDialog(self.phone_rep)
        if (phone_add.exec()):
            phone_d = self.phone_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            phonenumber = QTableWidgetItem(phone_d['phone_number'])
            phonenumber.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, phonenumber)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()), 'phone_number': edit_list[1].text()}
            self.phone_rep.set_dict(edit_d)
            phone_edit = PhoneAddDialog(self.phone_rep)
            if (phone_edit.exec()):
                phone_d = self.phone_rep.get_dict()
                phonenumber = QTableWidgetItem(phone_d['phone_number'])
                phonenumber.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, phonenumber)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_ph = {'id': int(del_list[0].text()),'phone_number': del_list[1].text()}
            self.phone_rep.del_phonenumber(del_ph)
            self.ui.tableWidget.removeRow(del_list[0].row())
    def click_cancel(self):
        self.accept()