from PyQt5.QtWidgets import QDialog

from Repository.Rep_Address import AddressRepository

from QT_view.AddressAddWin import Ui_AddressAdd

class AddressAddDialog(QDialog):
    def __init__(self,address_rep: AddressRepository):
        super(AddressAddDialog, self).__init__()
        self.address_rep = address_rep
        self.address_d = address_rep.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_AddressAdd()
        self.ui.setupUi(self)

        if (len(self.address_d['street'])):
            self.ui.lineEdit_street.setText(self.address_d['street'])

        if (len(self.address_d['home'])):
            self.ui.lineEdit_home.setText(self.address_d['home'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        a_street = self.ui.lineEdit_street.text()
        a_street = a_street.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        a_home = self.ui.lineEdit_home.text()
        a_home = a_home.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.address_d['id'] == -1):
            if (len(a_street)):
                self.address_d['street'] = a_street
                self.address_d['home'] = a_home
                self.address_d['id'] = self.address_rep.new_address(self.address_d)
                self.address_rep.set_dict(self.address_d)
                self.accept()
        else:
            if (len(a_street)):
                self.address_d['street'] = a_street
                self.address_d['home'] = a_home
                self.address_rep.update_address(self.address_d)
                self.address_rep.set_dict(self.address_d)
                self.accept()

    def click_cancel(self):
        self.reject()