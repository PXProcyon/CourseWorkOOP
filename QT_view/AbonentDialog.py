from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.AbonentAdd import AbonentAddDialog
from QT_view.AbonentWin import Ui_Dialog

from Repository.Rep_Abonent import AbonentRepository

class AbonentQt(QDialog):
    def __init__(self):
        super(AbonentQt, self).__init__()
        self.abonent_rep = AbonentRepository()
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

        abonent = self.abonent_rep.get_abonents()
        self.ui.tableWidget.setRowCount(len(abonent))
        row = 0
        for i in abonent:
            id_abonent = QTableWidgetItem(str(i['id']))
            id_abonent.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            last_name = QTableWidgetItem(i['last_name'])
            last_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            first_name = QTableWidgetItem(i['first_name'])
            first_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            patronymic = QTableWidgetItem(i['patronymic'])
            patronymic.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            age = QTableWidgetItem(str(i['age']))
            age.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_abonent)
            self.ui.tableWidget.setItem(row, 1, last_name)
            self.ui.tableWidget.setItem(row, 2, first_name)
            self.ui.tableWidget.setItem(row, 3, patronymic)
            self.ui.tableWidget.setItem(row, 4, age)
            row += 1

    def click_add(self):
        p_dict = {'id': -1, 'last_name': "", 'first_name': "", 'patronymic': "" , 'age': ""}
        self.abonent_rep.set_dict(p_dict)
        abonent_add = AbonentAddDialog(self.abonent_rep)

        if (abonent_add.exec()):
            abonent_d = self.abonent_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            last_name = QTableWidgetItem(abonent_d['last_name'])
            last_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            first_name = QTableWidgetItem(abonent_d['first_name'])
            first_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            patronymic = QTableWidgetItem(abonent_d['patronymic'])
            patronymic.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            age = QTableWidgetItem(abonent_d['age'])
            age.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, last_name)
            self.ui.tableWidget.setItem(count_row, 2, last_name)
            self.ui.tableWidget.setItem(count_row, 3, last_name)
            self.ui.tableWidget.setItem(count_row, 4, last_name)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()), 'last_name': edit_list[1].text(),
                      'first_name': edit_list[2].text(), 'patronymic': edit_list[3].text(), 'age': edit_list[4].text()}
            self.abonent_rep.set_dict(edit_d)
            abonent_edit = AbonentAddDialog(self.abonent_rep)
            if (abonent_edit.exec()):
                abonent_d = self.abonent_rep.get_dict()
                last_name = QTableWidgetItem(abonent_d['last_name'])
                last_name.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                first_name = QTableWidgetItem(abonent_d['first_name'])
                first_name.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                patronymic = QTableWidgetItem(abonent_d['patronymic'])
                patronymic.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                age = QTableWidgetItem(abonent_d['age'])
                age.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, last_name)
                self.ui.tableWidget.setItem(select_row, 2, last_name)
                self.ui.tableWidget.setItem(select_row, 3, last_name)
                self.ui.tableWidget.setItem(select_row, 4, last_name)
    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_ab = {'id': int(del_list[0].text()),'last_name': del_list[1].text(), 'first_name': del_list[2].text(),
                      'patronymic': del_list[3].text(), 'age': del_list[4].text()}
            self.ui.tableWidget.removeRow(del_list[0].row())
            self.abonent_rep.del_abonent(del_ab)

    def click_cancel(self):
        self.accept()
