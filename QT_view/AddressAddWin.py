from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddressAdd(object):
    def setupUi(self, AddressAdd):
        AddressAdd.setObjectName("AbonentAdd")
        AddressAdd.resize(311, 79)
        AddressAdd.setMinimumSize(QtCore.QSize(350, 115))
        AddressAdd.setMaximumSize(QtCore.QSize(350, 115))

        """Labels"""

        self.label_street = QtWidgets.QLabel(AddressAdd)
        self.label_street.setGeometry(QtCore.QRect(10, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_home = QtWidgets.QLabel(AddressAdd)
        self.label_home.setGeometry(QtCore.QRect(10, 40, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Поля для ввода"""



        self.lineEdit_street = QtWidgets.QLineEdit(AddressAdd)
        self.lineEdit_street.setGeometry(QtCore.QRect(120, 10, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_home = QtWidgets.QLineEdit(AddressAdd)
        self.lineEdit_home.setGeometry(QtCore.QRect(120, 40, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(AddressAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 75, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AddressAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 75, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(AddressAdd)
        QtCore.QMetaObject.connectSlotsByName(AddressAdd)

    def retranslateUi(self, AddressAdd):
        _translate = QtCore.QCoreApplication.translate
        AddressAdd.setWindowTitle(_translate("AddressAdd", "Ввод адреса абонента"))

        self.label_street.setText(_translate("AddressAdd", "Улица абонента:"))
        self.label_home.setText(_translate("AddressAdd", "Дом абонента:"))

        self.pushButton.setText(_translate("AddressAdd", "Добавить"))
        self.pushButton_2.setText(_translate("AddressAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddressAdd = QtWidgets.QDialog()
    ui = Ui_AddressAdd()
    ui.setupUi(AddressAdd)
    AddressAdd.show()
    sys.exit(app.exec_())
