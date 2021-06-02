from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AbonentAdd(object):
    def setupUi(self, AbonentAdd):
        AbonentAdd.setObjectName("AbonentAdd")
        AbonentAdd.resize(311, 79)
        AbonentAdd.setMinimumSize(QtCore.QSize(350, 200))
        AbonentAdd.setMaximumSize(QtCore.QSize(350, 200))

        """Labels"""

        self.label_last_name = QtWidgets.QLabel(AbonentAdd)
        self.label_last_name.setGeometry(QtCore.QRect(10, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_first_name = QtWidgets.QLabel(AbonentAdd)
        self.label_first_name.setGeometry(QtCore.QRect(10, 40, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_patronymic = QtWidgets.QLabel(AbonentAdd)
        self.label_patronymic.setGeometry(QtCore.QRect(10, 80, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.label_age = QtWidgets.QLabel(AbonentAdd)
        self.label_age.setGeometry(QtCore.QRect(10, 120, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Поля для ввода"""



        self.lineEdit_last_name = QtWidgets.QLineEdit(AbonentAdd)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(120, 10, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_first_name = QtWidgets.QLineEdit(AbonentAdd)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(120, 40, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_patronymic = QtWidgets.QLineEdit(AbonentAdd)
        self.lineEdit_patronymic.setGeometry(QtCore.QRect(120, 80, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.lineEdit_age = QtWidgets.QLineEdit(AbonentAdd)
        self.lineEdit_age.setGeometry(QtCore.QRect(120, 120, 220, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)


        """Кнопки"""

        self.pushButton = QtWidgets.QPushButton(AbonentAdd)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(AbonentAdd)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(AbonentAdd)
        QtCore.QMetaObject.connectSlotsByName(AbonentAdd)

    def retranslateUi(self, AbonentAdd):
        _translate = QtCore.QCoreApplication.translate
        AbonentAdd.setWindowTitle(_translate("AbonentAdd", "Ввод данных абонента"))
        self.label_last_name.setText(_translate("AbonentAdd", "Фамилия абонента:"))
        self.label_first_name.setText(_translate("AbonentAdd", "Имя абонента:"))
        self.label_patronymic.setText(_translate("AbonentAdd", "Отчество абонента:"))
        self.label_age.setText(_translate("AbonentAdd", "Возраст абонента:"))
        self.pushButton.setText(_translate("AbonentAdd", "Добавить"))
        self.pushButton_2.setText(_translate("AbonentAdd", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AbonentAdd = QtWidgets.QDialog()
    ui = Ui_AbonentAdd()
    ui.setupUi(AbonentAdd)
    AbonentAdd.show()
    sys.exit(app.exec_())
