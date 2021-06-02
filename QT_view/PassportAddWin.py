from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PassportAdd(object):
    def setupUi(self, PassportAdd):
        PassportAdd.setObjectName("PassportAdd")
        PassportAdd.resize(311, 79)
        PassportAdd.setMinimumSize(QtCore.QSize(350, 110))
        PassportAdd.setMaximumSize(QtCore.QSize(350, 110))

        """Labels"""

        self.label_serial = QtWidgets.QLabel(PassportAdd)
        self.label_serial.setGeometry(QtCore.QRect(10, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_number = QtWidgets.QLabel(PassportAdd)
        self.label_number.setGeometry(QtCore.QRect(10, 40, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Поля для ввода"""

        self.lineEdit_serial = QtWidgets.QLineEdit(PassportAdd)
        self.lineEdit_serial.setGeometry(QtCore.QRect(120, 10, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_number = QtWidgets.QLineEdit(PassportAdd)
        self.lineEdit_number.setGeometry(QtCore.QRect(120, 40, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(PassportAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PassportAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 70, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(PassportAdd)
        QtCore.QMetaObject.connectSlotsByName(PassportAdd)

    def retranslateUi(self, AbonentAdd):
        _translate = QtCore.QCoreApplication.translate
        AbonentAdd.setWindowTitle(_translate("AbonentAdd", "Ввод данных абонента"))
        self.label_serial.setText(_translate("AbonentAdd", "Серия паспорта:"))
        self.label_number.setText(_translate("AbonentAddd", "Номер паспорта:"))
        self.pushButton.setText(_translate("AbonentAdd", "Добавить"))
        self.pushButton_2.setText(_translate("AbonentAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PassportAdd = QtWidgets.QDialog()
    ui = Ui_PassportAdd()
    ui.setupUi(PassportAdd)
    PassportAdd.show()
    sys.exit(app.exec_())
