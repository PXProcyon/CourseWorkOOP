from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CityAdd(object):
    def setupUi(self, CityAdd):
        CityAdd.setObjectName("CityAdd")
        CityAdd.resize(311, 79)
        CityAdd.setMinimumSize(QtCore.QSize(350, 80))
        CityAdd.setMaximumSize(QtCore.QSize(350, 80))

        self.label_city = QtWidgets.QLabel(CityAdd)
        self.label_city.setGeometry(QtCore.QRect(10, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_city = QtWidgets.QLineEdit(CityAdd)
        self.lineEdit_city.setGeometry(QtCore.QRect(120, 10, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton = QtWidgets.QPushButton(CityAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(CityAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 40, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(CityAdd)
        QtCore.QMetaObject.connectSlotsByName(CityAdd)

    def retranslateUi(self, CityAdd):
        _translate = QtCore.QCoreApplication.translate
        CityAdd.setWindowTitle(_translate("CityAdd", "Ввод города абонента"))
        self.label_city.setText(_translate("CityAdd", "Город абонента:"))
        self.pushButton.setText(_translate("CityAdd", "Добавить"))
        self.pushButton_2.setText(_translate("CityAdd", "Отмена"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CityAdd = QtWidgets.QDialog()
    ui = Ui_CityAdd()
    ui.setupUi(CityAdd)
    CityAdd.show()
    sys.exit(app.exec_())