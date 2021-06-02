from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.PassportAdd import PassportAddDialog
from QT_view.PassportWin import Ui_Dialog

from Repository.Rep_Passport import PassportRepository

class PassportQt(QDialog):
    def __init__(self):
        super(PassportQt, self).__init__()
        self.passport_rep = PassportRepository()
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

        passport = self.passport_rep.get_passports()
        self.ui.tableWidget.setRowCount(len(passport))
        row = 0
        for i in passport:
            id_passport = QTableWidgetItem(str(i['id']))
            id_passport.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            serial_passport = QTableWidgetItem(i['serial'])
            serial_passport.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            number_passport = QTableWidgetItem(i['number'])
            number_passport.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_passport)
            self.ui.tableWidget.setItem(row, 1, serial_passport)
            self.ui.tableWidget.setItem(row, 2, number_passport)
            row += 1

    def click_add(self):
        p_dict = {'id': -1, 'serial': "", 'number': ""}
        self.passport_rep.set_dict(p_dict)
        passport_add = PassportAddDialog(self.passport_rep)
        if (passport_add.exec()):
            passport_d = self.passport_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            id_passport = QTableWidgetItem(str(passport_d['id']))
            id_passport.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            serial = QTableWidgetItem(passport_d['serial'])
            serial.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            number = QTableWidgetItem(passport_d['number'])
            number.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 0, id_passport)
            self.ui.tableWidget.setItem(count_row, 1, serial)
            self.ui.tableWidget.setItem(count_row, 2, number)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()), 'serial': edit_list[1].text(), 'number': edit_list[2].text()}
            self.passport_rep.set_dict(edit_d)
            passport_edit = PassportAddDialog(self.passport_rep)
            if (passport_edit.exec()):
                passport_d = self.passport_rep.get_dict()
                id_passport = QTableWidgetItem(str(passport_d['id']))
                id_passport.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                serial = QTableWidgetItem(passport_d['serial'])
                serial.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                number = QTableWidgetItem(passport_d['number'])
                number.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 0, id_passport)
                self.ui.tableWidget.setItem(select_row, 1, serial)
                self.ui.tableWidget.setItem(select_row, 2, number)
    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_p = {'id': int(del_list[0].text()), 'serial': del_list[1].text(), 'number': del_list[2].text()}
            self.passport_rep.del_passport(del_p)
            self.ui.tableWidget.removeRow(del_list[0].row())
    def click_cancel(self):
        self.accept()