from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from QT_view.SimcardAdd import SimcardAddDialog
from QT_view.SimcardDialog import Ui_Dialog
from Repository.Rep_SimCard import SimCardRepository

class SimcardQt(QDialog):
    def __init__(self):
        super(SimcardQt, self).__init__()
        self.simcard_rep = SimCardRepository()
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

        sim_card = self.simcard_rep.get_simcards()
        self.ui.tableWidget.setRowCount(len(sim_card))
        row = 0
        for i in sim_card:
            id_simcard = QTableWidgetItem(str(i['id']))
            id_simcard.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            iccim = QTableWidgetItem(str(i['ICCIM']))
            iccim.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_simcard)
            self.ui.tableWidget.setItem(row, 1, iccim)
            row += 1

    def click_add(self):
        p_dict = {'id': -1,'ICCIM': ""}
        self.simcard_rep.set_dict(p_dict)
        simcard_add = SimcardAddDialog( self.simcard_rep)
        if (simcard_add.exec()):
            simcard_d = self.simcard_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            iccim = QTableWidgetItem(simcard_d['ICCIM'])
            iccim.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, iccim)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()),'ICCIM': edit_list[1].text()}
            self.simcard_rep.set_dict(edit_d)
            simcard_edit = SimcardAddDialog(self.simcard_rep)
            if (simcard_edit.exec()):
                simcard_d = self.simcard_rep.get_dict()
                iccim = QTableWidgetItem(simcard_d['ICCIM'])
                iccim.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, iccim)
    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_s = {'id': int(del_list[0].text()),'ICCIM': del_list[1].text()}
            self.simcard_rep.del_simcard(del_s)
            self.ui.tableWidget.removeRow(del_list[0].row())

    def click_cancel(self):
        self.accept()