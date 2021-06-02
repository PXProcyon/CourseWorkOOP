from PyQt5.QtWidgets import QDialog

from Repository.Rep_Passport import PassportRepository
from QT_view.PassportAddWin import Ui_PassportAdd

class PassportAddDialog(QDialog):
    def __init__(self, passport_rep: PassportRepository):
        super(PassportAddDialog, self).__init__()
        self.passport_rep = passport_rep
        self.passport_d = passport_rep.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_PassportAdd()
        self.ui.setupUi(self)

        if (len(self.passport_d['serial'])):
            self.ui.lineEdit_serial.setText(self.passport_d['serial'])

        if (len(self.passport_d['number'])):
            self.ui.lineEdit_number.setText(self.passport_d['number'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        s_passport = self.ui.lineEdit_serial.text()
        s_passport = s_passport.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        n_passport = self.ui.lineEdit_number.text()
        n_passport = n_passport.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.passport_d['id'] == -1):
            if (len(n_passport)):
                self.passport_d['serial'] = s_passport
                self.passport_d['number'] = n_passport
                self.passport_d['id'] = self.passport_rep.new_passport(self.passport_d)
                self.passport_rep.set_dict(self.passport_d)
                self.accept()
        else:
            if (len(n_passport)):
                self.passport_d['serial'] = s_passport
                self.passport_d['number'] = n_passport
                self.passport_rep.update_passport(self.passport_d)
                self.passport_rep.set_dict(self.passport_d)
                self.accept()

    def click_cancel(self):
        self.reject()