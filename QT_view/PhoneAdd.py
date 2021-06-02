from PyQt5.QtWidgets import QDialog

from Repository.Rep_PhoneNumber import PhoneNumberRepository

from QT_view.PhoneAddWin import Ui_PhoneAdd

class PhoneAddDialog(QDialog):
    def __init__(self, rep_phone: PhoneNumberRepository):
        super(PhoneAddDialog, self).__init__()
        self.phone_rep = rep_phone
        self.phone_d = rep_phone.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_PhoneAdd()
        self.ui.setupUi(self)

        if (len(self.phone_d['phone_number'])):
            self.ui.lineEdit_phone_number.setText(self.phone_d['phone_number'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        p_phone = self.ui.lineEdit_phone_number.text()
        p_phone = p_phone.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.phone_d['id'] == -1):
            if (len(p_phone)):
                self.phone_d['phone_number'] = p_phone
                self.phone_d['id'] = self.phone_rep.new_phonenumber(self.phone_d)
                self.phone_rep.set_dict(self.phone_d)
                self.accept()
        else:
            if (len(p_phone)):
                self.phone_d['phone_number'] = p_phone
                self.phone_rep.update_phonenumber(self.phone_d)
                self.phone_rep.set_dict(self.phone_d)
                self.accept()

    def click_cancel(self):
        self.reject()
