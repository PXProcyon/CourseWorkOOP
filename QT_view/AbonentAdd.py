from PyQt5.QtWidgets import QDialog

from Repository.Rep_Abonent import AbonentRepository

from QT_view.AbonentAddWin import Ui_AbonentAdd

class AbonentAddDialog(QDialog):
    def __init__(self, abonent_rep: AbonentRepository):
        super(AbonentAddDialog, self).__init__()
        self.abonent_rep = abonent_rep
        self.abonent_d = abonent_rep.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_AbonentAdd()
        self.ui.setupUi(self)

        if (len(self.abonent_d['last_name'])):
            self.ui.lineEdit_last_name.setText(self.abonent_d['last_name'])

        if (len(self.abonent_d['first_name'])):
            self.ui.lineEdit_first_name.setText(self.abonent_d['first_name'])

        if (len(self.abonent_d['patronymic'])):
            self.ui.lineEdit_patronymic.setText(self.abonent_d['patronymic'])

        if (len(self.abonent_d['age'])):
            self.ui.lineEdit_age.setText(self.abonent_d['age'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        ab_last_name = self.ui.lineEdit_last_name.text()
        ab_last_name = ab_last_name.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        ab_first_name = self.ui.lineEdit_first_name.text()
        ab_first_name = ab_first_name.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        ab_patronymic = self.ui.lineEdit_patronymic.text()
        ab_patronymic = ab_patronymic.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        ab_age = self.ui.lineEdit_age.text()
        ab_age = ab_age.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.abonent_d['id'] == -1):
            if (len(ab_last_name)):
                self.abonent_d['last_name'] = ab_last_name
                self.abonent_d['first_name'] = ab_first_name
                self.abonent_d['patronymic'] = ab_patronymic
                self.abonent_d['age'] = ab_age
                self.abonent_d['id'] = self.abonent_rep.new_abonent(self.abonent_d)
                self.abonent_rep.set_dict(self.abonent_d)
                self.accept()
        else:
            if (len(ab_last_name)):
                self.abonent_d['last_name'] = ab_last_name
                self.abonent_d['first_name'] = ab_first_name
                self.abonent_d['patronymic'] = ab_patronymic
                self.abonent_d['age'] = ab_age
                self.abonent_rep.update_abonent(self.abonent_d)
                self.abonent_rep.set_dict(self.abonent_d)
                self.accept()
    def click_cancel(self):
        self.reject()