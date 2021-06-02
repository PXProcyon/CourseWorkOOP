from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PhoneAdd(object):
    def setupUi(self, PhoneAdd):
        PhoneAdd.setObjectName("PhoneAdd")
        PhoneAdd.resize(311, 79)
        PhoneAdd.setMinimumSize(QtCore.QSize(350, 80))
        PhoneAdd.setMaximumSize(QtCore.QSize(350, 80))

        """Labels"""

        self.label_phone_number = QtWidgets.QLabel(PhoneAdd)
        self.label_phone_number.setGeometry(QtCore.QRect(10, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        """Поля для ввода"""


        self.lineEdit_phone_number = QtWidgets.QLineEdit(PhoneAdd)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(120, 10, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(PhoneAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PhoneAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 40, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(PhoneAdd)
        QtCore.QMetaObject.connectSlotsByName(PhoneAdd)

    def retranslateUi(self, PhoneAdd):
        _translate = QtCore.QCoreApplication.translate
        PhoneAdd.setWindowTitle(_translate("PhoneAdd", "Ввод данных абонента"))
        self.label_phone_number.setText(_translate("PhoneAdd", "Номер телефона:"))
        self.pushButton.setText(_translate("PhoneAdd", "Добавить"))
        self.pushButton_2.setText(_translate("PhoneAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PhoneAdd = QtWidgets.QDialog()
    ui = Ui_PhoneAdd()
    ui.setupUi(PhoneAdd)
    PhoneAdd.show()
    sys.exit(app.exec_())
