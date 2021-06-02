from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Contract(object):
    def setupUi(self, ContractAdd):
        ContractAdd.setObjectName("ContractAdd")
        ContractAdd.resize(311, 79)
        ContractAdd.setMinimumSize(QtCore.QSize(350, 160))
        ContractAdd.setMaximumSize(QtCore.QSize(350, 160))

        """Labels"""

        self.label_date = QtWidgets.QLabel(ContractAdd)
        self.label_date.setGeometry(QtCore.QRect(10, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_number_contract = QtWidgets.QLabel(ContractAdd)
        self.label_number_contract.setGeometry(QtCore.QRect(10, 40, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_number_abonent = QtWidgets.QLabel(ContractAdd)
        self.label_number_abonent.setGeometry(QtCore.QRect(10, 80, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        """Поля для ввода"""



        self.lineEdit_date = QtWidgets.QLineEdit(ContractAdd)
        self.lineEdit_date.setGeometry(QtCore.QRect(120, 10, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_number_contract = QtWidgets.QLineEdit(ContractAdd)
        self.lineEdit_number_contract.setGeometry(QtCore.QRect(120, 40, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_number_abonent = QtWidgets.QLineEdit(ContractAdd)
        self.lineEdit_number_abonent.setGeometry(QtCore.QRect(120, 80, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(ContractAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ContractAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 120, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(ContractAdd)
        QtCore.QMetaObject.connectSlotsByName(ContractAdd)

    def retranslateUi(self, AbonentAdd):
        _translate = QtCore.QCoreApplication.translate
        AbonentAdd.setWindowTitle(_translate("AbonentAdd", "Ввод данных абонента"))
        self.label_date.setText(_translate("AbonentAdd", "Дата контракта:"))
        self.label_number_contract.setText(_translate("AbonentAdd", "Номер контракта:"))
        self.label_number_abonent.setText(_translate("AbonentAdd", "Номер абонента: "))
        self.pushButton.setText(_translate("AbonentAdd", "Добавить"))
        self.pushButton_2.setText(_translate("AbonentAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ContractAdd = QtWidgets.QDialog()
    ui = Ui_Contract()
    ui.setupUi(ContractAdd)
    ContractAdd.show()
    sys.exit(app.exec_())