from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangelogAdd(object):
    def setupUi(self, ChangelogAdd):
        ChangelogAdd.setObjectName("ChangelogAdd")
        ChangelogAdd.resize(311, 79)
        ChangelogAdd.setMinimumSize(QtCore.QSize(550, 130))
        ChangelogAdd.setMaximumSize(QtCore.QSize(550, 130))

        """Labels"""

        self.label_data_change = QtWidgets.QLabel(ChangelogAdd)
        self.label_data_change.setGeometry(QtCore.QRect(10, 10, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_content = QtWidgets.QLabel(ChangelogAdd)
        self.label_content.setGeometry(QtCore.QRect(10, 40, 223, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Поля для ввода"""


        self.lineEdit_data_change = QtWidgets.QLineEdit(ChangelogAdd)
        self.lineEdit_data_change.setGeometry(QtCore.QRect(190, 10, 190, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_content = QtWidgets.QLineEdit(ChangelogAdd)
        self.lineEdit_content.setGeometry(QtCore.QRect(230, 40, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(ChangelogAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ChangelogAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 80, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(ChangelogAdd)
        QtCore.QMetaObject.connectSlotsByName(ChangelogAdd)

    def retranslateUi(self, ChangelogAdd):
        _translate = QtCore.QCoreApplication.translate
        ChangelogAdd.setWindowTitle(_translate("ChangelogAdd", "Ввод данных тарифа"))
        self.label_data_change.setText(_translate("ChangelogAdd", "Введите дату изменения тарифа:"))
        self.label_content.setText(_translate("ChangelogAdd", "Введите содержимое текущего изменения тарифа:"))
        self.pushButton.setText(_translate("ChangelogAdd", "Добавить"))
        self.pushButton_2.setText(_translate("ChangelogAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ChangelogAdd = QtWidgets.QDialog()
    ui = Ui_ChangelogAdd()
    ui.setupUi(ChangelogAdd)
    ChangelogAdd.show()
    sys.exit(app.exec_())