from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from Repository.Rep_Changelog import ChangelogRepository
from QT_view.ChangelogDialog import Ui_Dialog
from QT_view.ChangelogAdd import ChangelogAddDialog

class ChangelogQt(QDialog):
    def __init__(self):
        super(ChangelogQt, self).__init__()
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

        changelog = self.changelog_rep.get_changelogs()
        self.ui.tableWidget.setRowCount(len(changelog))
        row = 0
        for i in changelog:
            id_changelog = QTableWidgetItem(str(i['id']))
            id_changelog.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            data_change = QTableWidgetItem(i['data_change'])
            data_change.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            content = QTableWidgetItem(i['content'])
            content.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(row, 0, id_changelog)
            self.ui.tableWidget.setItem(row, 1, data_change)
            self.ui.tableWidget.setItem(row, 2, content)
            row += 1

    def click_add(self):
        p_dict = {'id': -1, 'data_change': "", 'content': ""}
        self.changelog_rep.set_dict(p_dict)
        changelog_add = ChangelogAddDialog(self.changelog_rep)
        if (changelog_add.exec()):
            changelog_d = self.changelog_rep.get_dict()
            count_row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count_row + 1)
            data_change = QTableWidgetItem(changelog_d['data_change'])
            data_change.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            content = QTableWidgetItem(changelog_d['content'])
            content.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            )
            self.ui.tableWidget.setItem(count_row, 1, data_change)
            self.ui.tableWidget.setItem(count_row, 2, content)

    def click_edit(self):
        edit_list = self.ui.tableWidget.selectedItems()
        if (len(edit_list)):
            select_row = self.ui.tableWidget.currentRow()
            edit_d = {'id': int(edit_list[0].text()),'data_change': edit_list[9].text(),'content': edit_list[10].text()}
            self.changelog_rep.set_dict(edit_d)
            changelog_edit = ChangelogAddDialog(self.changelog_rep)
            if (changelog_edit.exec()):
                changelog_d = self.changelog_rep.get_dict()
                data_change = QTableWidgetItem(changelog_d['translate_number'])
                data_change.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                content = QTableWidgetItem(changelog_d['content'])
                content.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
                self.ui.tableWidget.setItem(select_row, 1, data_change)
                self.ui.tableWidget.setItem(select_row, 2, content)

    def click_del(self):
        del_list = self.ui.tableWidget.selectedItems()
        if (len(del_list)):
            del_cha = {'id': int(del_list[0].text()),'Дата изменения': del_list[1].text(),'Содержимое изменения': del_list[2].text()}
            self.ui.tableWidget.removeRow(del_list[0].row())
            self.changelog_rep.del_changelog(del_cha)

    def click_cancel(self):
        self.accept()