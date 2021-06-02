from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TarifAdd(object):
    def setupUi(self, TarifAdd):
        TarifAdd.setObjectName("TarifAdd")
        TarifAdd.resize(311, 79)
        TarifAdd.setMinimumSize(QtCore.QSize(550, 300))
        TarifAdd.setMaximumSize(QtCore.QSize(550, 300))

        """Labels"""

        self.label_tarif_name = QtWidgets.QLabel(TarifAdd)
        self.label_tarif_name.setGeometry(QtCore.QRect(10, 10, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_anothet_minute = QtWidgets.QLabel(TarifAdd)
        self.label_anothet_minute.setGeometry(QtCore.QRect(10, 40, 275, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_home_minute = QtWidgets.QLabel(TarifAdd)
        self.label_home_minute.setGeometry(QtCore.QRect(10, 70, 290, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_sms = QtWidgets.QLabel(TarifAdd)
        self.label_sms.setGeometry(QtCore.QRect(10, 100, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_internet = QtWidgets.QLabel(TarifAdd)
        self.label_internet.setGeometry(QtCore.QRect(10, 130, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_speed_internet = QtWidgets.QLabel(TarifAdd)
        self.label_speed_internet.setGeometry(QtCore.QRect(10, 160, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_cost = QtWidgets.QLabel(TarifAdd)
        self.label_cost.setGeometry(QtCore.QRect(10, 190, 220, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_transition_number = QtWidgets.QLabel(TarifAdd)
        self.label_transition_number.setGeometry(QtCore.QRect(10, 220, 180, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        """Поля для ввода"""

        self.lineEdit_tarif_name = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_tarif_name.setGeometry(QtCore.QRect(170, 10, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_another_minute = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_another_minute.setGeometry(QtCore.QRect(290, 40, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_home_minute = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_home_minute.setGeometry(QtCore.QRect(305, 70, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_sms = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_sms.setGeometry(QtCore.QRect(120, 100, 230, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_internet = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_internet.setGeometry(QtCore.QRect(220, 130, 230, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_speed_internet = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_speed_internet.setGeometry(QtCore.QRect(222, 160, 230, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_cost = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_cost.setGeometry(QtCore.QRect(165, 190, 190, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_translate_number = QtWidgets.QLineEdit(TarifAdd)
        self.lineEdit_translate_number.setGeometry(QtCore.QRect(200, 220, 190, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(TarifAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(TarifAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 260, 81, 31))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(TarifAdd)
        QtCore.QMetaObject.connectSlotsByName(TarifAdd)

    def retranslateUi(self, TarifAdd):
        _translate = QtCore.QCoreApplication.translate
        TarifAdd.setWindowTitle(_translate("AbonentAdd", "Ввод данных тарифа"))
        self.label_tarif_name.setText(_translate("AbonentAdd", "Введите название тарифа:"))
        self.label_anothet_minute.setText(_translate("AbonentAddd", "Введите кол-во минут на номера других операторов:"))
        self.label_home_minute.setText(_translate("AbonentAdd", "Введите кол-во минут на номера домащнего оператора:"))
        self.label_sms.setText(_translate("AbonentAdd", "Введите кол-во смс:"))
        self.label_internet.setText(_translate("AbonentAdd", "Введите кол-во интернет-соединения:"))
        self.label_speed_internet.setText(_translate("AbonentAdd", "Введите скорость интернет-соединения:"))
        self.label_cost.setText(_translate("AbonentAdd", "Введите стоимость тарифа:"))
        self.label_transition_number.setText(_translate("AbonentAdd", "Введите номер перехода на тариф:"))
        self.pushButton.setText(_translate("AbonentAdd", "Добавить"))
        self.pushButton_2.setText(_translate("AbonentAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TarifAdd = QtWidgets.QDialog()
    ui = Ui_TarifAdd()
    ui.setupUi(TarifAdd)
    TarifAdd.show()
    sys.exit(app.exec_())
