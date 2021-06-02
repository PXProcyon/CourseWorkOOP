from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimcardAdd(object):
    def setupUi(self, SimcardAdd):
        SimcardAdd.setObjectName("SimcardAdd")
        SimcardAdd.resize(311, 79)
        SimcardAdd.setMinimumSize(QtCore.QSize(350, 80))
        SimcardAdd.setMaximumSize(QtCore.QSize(350, 80))

        """Labels"""

        self.label_ICCIM = QtWidgets.QLabel(SimcardAdd)
        self.label_ICCIM.setGeometry(QtCore.QRect(10, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        """Поля для ввода"""

        self.lineEdit_ICCIM = QtWidgets.QLineEdit(SimcardAdd)
        self.lineEdit_ICCIM.setGeometry(QtCore.QRect(140, 10, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(SimcardAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SimcardAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 40, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(SimcardAdd)
        QtCore.QMetaObject.connectSlotsByName(SimcardAdd)

    def retranslateUi(self, SimcardAdd):
        _translate = QtCore.QCoreApplication.translate
        SimcardAdd.setWindowTitle(_translate("SimcardAdd", "Ввод данных абонента"))
        self.label_ICCIM.setText(_translate("AbonentAdd", "Номер ICCIM сим-карты::"))
        self.pushButton.setText(_translate("AbonentAdd", "Добавить"))
        self.pushButton_2.setText(_translate("AbonentAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SimcardAdd = QtWidgets.QDialog()
    ui = Ui_SimcardAdd()
    ui.setupUi(SimcardAdd)
    SimcardAdd.show()
    sys.exit(app.exec_())
