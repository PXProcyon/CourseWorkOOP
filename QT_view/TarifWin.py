from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.TarifAdd import TarifAddDialog
from QT_view.TarifDialog import Ui_Dialog
from Repository.Rep_Tarif import TarifRepository
from Repository.Rep_Changelog import ChangelogRepository

class TarifQt(QDialog):
    def __init__(self):
        super(TarifQt, self).__init__()
        self.tarif_rep = TarifRepository()
        self.changelog_rep = ChangelogRepository()
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

        tarif = self.tarif_rep.get_tarifs()
        self.ui.tableWidget.setRowCount(len(tarif))
        row = 0
        for i in tarif:
            id_tarif = QTableWidgetItem(str(i['id']))
            id_tarif.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            tarif_name = QTableWidgetItem(i['tarif_name'])
            tarif_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            another_minute = QTableWidgetItem(str(i['anothet_minute']))
            another_minute.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            home_minute = QTableWidgetItem(str(i['home_minute']))
            home_minute.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            sms = QTableWidgetItem(str(i['sms']))
            sms.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            internet = QTableWidgetItem(i['internet'])
            internet.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            speed_internet = QTableWidgetItem(i['speed_internet'])
            speed_internet.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            cost = QTableWidgetItem(i['cost'])
            cost.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            translate_number = QTableWidgetItem(i['transition_number'])
            translate_number.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_tarif)
            self.ui.tableWidget.setItem(row, 1, tarif_name)
            self.ui.tableWidget.setItem(row, 2, another_minute)
            self.ui.tableWidget.setItem(row, 3, home_minute)
            self.ui.tableWidget.setItem(row, 4, sms)
            self.ui.tableWidget.setItem(row, 5, internet)
            self.ui.tableWidget.setItem(row, 6, speed_internet)
            self.ui.tableWidget.setItem(row, 7, cost)
            self.ui.tableWidget.setItem(row, 8, translate_number)
            row += 1



    def click_add(self):
        p_dict = {'id': -1, 'tarif_name': "", 'another_minute': "",
                  'home_minute': "",'sms': "",'internet': "",'speed_internet': "",
                 'cost': "",'translate_number': ""}
        self.tarif_rep.set_dict(p_dict)
        tarif_add = TarifAddDialog(self.tarif_rep)
        if (tarif_add.exec()):
            tarif_d = self.tarif_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            tarif_name = QTableWidgetItem(tarif_d['tarif_name'])
            tarif_name.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            another_minute = QTableWidgetItem(tarif_d['another_minute'])
            another_minute.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            home_minute = QTableWidgetItem(tarif_d['home_minute'])
            home_minute.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            sms = QTableWidgetItem(tarif_d['sms'])
            sms.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            internet = QTableWidgetItem(tarif_d['internet'])
            internet.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            speed_internet = QTableWidgetItem(tarif_d['speed_internet'])
            speed_internet.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            cost = QTableWidgetItem(tarif_d['cost'])
            cost.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            translate_number = QTableWidgetItem(tarif_d['translate_number'])
            translate_number.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, tarif_name)
            self.ui.tableWidget.setItem(count_row, 2, another_minute)
            self.ui.tableWidget.setItem(count_row, 3, home_minute)
            self.ui.tableWidget.setItem(count_row, 4, sms)
            self.ui.tableWidget.setItem(count_row, 5, internet)
            self.ui.tableWidget.setItem(count_row, 6, speed_internet)
            self.ui.tableWidget.setItem(count_row, 7, cost)
            self.ui.tableWidget.setItem(count_row, 8, translate_number)




    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()), 'tarif_name': edit_list[1].text(), 'another_minute': edit_list[2].text(),
                      'home_minute': edit_list[3].text(),'sms': edit_list[4].text(),'internet': edit_list[5].text(),
                      'speed_internet': edit_list[6].text(),'cost': edit_list[7].text(),
                     'translate_number': edit_list[8].text()}
            self.tarif_rep.set_dict(edit_d)
            tarif_edit = TarifAddDialog(self.tarif_rep)

            if (tarif_edit.exec()):
                tarif_d = self.tarif_rep.get_dict()
                tarif_name = QTableWidgetItem(tarif_d['tarif_name'])
                tarif_name.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                another_minute = QTableWidgetItem(tarif_d['another_minute'])
                another_minute.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                home_minute = QTableWidgetItem(tarif_d['home_minute'])
                home_minute.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                sms = QTableWidgetItem(tarif_d['sms'])
                sms.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                internet = QTableWidgetItem(tarif_d['internet'])
                internet.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                speed_internet = QTableWidgetItem(tarif_d['speed_internet'])
                speed_internet.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                cost = QTableWidgetItem(tarif_d['cost'])
                cost.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                translate_number = QTableWidgetItem(tarif_d['translate_number'])
                translate_number.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, tarif_name)
                self.ui.tableWidget.setItem(select_row, 2, another_minute)
                self.ui.tableWidget.setItem(select_row, 3, home_minute)
                self.ui.tableWidget.setItem(select_row, 4, sms)
                self.ui.tableWidget.setItem(select_row, 5, internet)
                self.ui.tableWidget.setItem(select_row, 6, speed_internet)
                self.ui.tableWidget.setItem(select_row, 7, cost)
                self.ui.tableWidget.setItem(select_row, 8, translate_number)



    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_t = {'id': int(del_list[0].text()), 'Название тарифа': del_list[1].text(), 'Кол-во минут на номера других операторов': del_list[2].text(),
                      'кол-во минут на номера домащнего оператора': del_list[3].text(),'Кол-во смс': del_list[4].text(),'Количество интернета': del_list[5].text(),
                      'Скорость интернета': del_list[6].text(),'Стоимость тарифа': del_list[7].text(),
                     'Номер перехода на тариф': del_list[8].text()}

            self.tarif_rep.del_tarif(del_t)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()