from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.CityAdd import CityAddDialog
from QT_view.CityWin import Ui_Dialog

from Repository.Rep_City import CityRepository

class CityQt(QDialog):
    def __init__(self):
        super(CityQt, self).__init__()
        self.city_rep = CityRepository()
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

        city = self.city_rep.get_citys()
        self.ui.tableWidget.setRowCount(len(city))
        row = 0
        for i in city:
            id_city = QTableWidgetItem(str(i['id']))
            id_city.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            city_name = QTableWidgetItem(i['city_name'])
            city_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_city)
            self.ui.tableWidget.setItem(row, 1, city_name)
            row += 1

    def click_add(self):
        p_dict = {'id': -1,'city_name': ""}
        self.city_rep.set_dict(p_dict)
        city_add = CityAddDialog(self.city_rep)
        if (city_add.exec()):
            city_d = self.city_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            id_city = QTableWidgetItem(str(city_d['id']))
            id_city.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            city_name = QTableWidgetItem(city_d['city_name'])
            city_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, city_name)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()),'city_name': edit_list[1].text()}
            self.city_rep.set_dict(edit_d)
            city_edit = CityAddDialog(self.city_rep)
            if (city_edit.exec()):
                city_d = self.city_rep.get_dict()
                id_city = QTableWidgetItem(str(city_d['id']))
                id_city.setFlags(
                     QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                city_name = QTableWidgetItem(city_d['city_name'])
                city_name.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, city_name)
    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_c = {'id': int(del_list[0].text()),'city_name': del_list[1].text()}
            self.city_rep.del_city(del_c)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()