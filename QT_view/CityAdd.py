from PyQt5.QtWidgets import QDialog

from Repository.Rep_City import CityRepository
from QT_view.CityAddWin import Ui_CityAdd

class CityAddDialog(QDialog):
    def __init__(self,city_rep: CityRepository):
        super(CityAddDialog, self).__init__()
        self.city_rep = city_rep
        self.city_d = city_rep.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_CityAdd()
        self.ui.setupUi(self)

        if (len(self.city_d['city_name'])):
            self.ui.lineEdit_city.setText(self.city_d['city_name'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        c_city = self.ui.lineEdit_city.text()
        c_city = c_city.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.city_d['id'] == -1):
            if (len(c_city)):
                self.city_d['city_name'] = c_city
                self.city_d['id'] = self.city_rep.new_city(self.city_d)
                self.city_rep.set_dict(self.city_d)
                self.accept()
        else:
            if (len(c_city)):
                self.city_d['city_name'] = c_city
                self.city_rep.update_city(self.city_d)
                self.city_rep.set_dict(self.city_d)
                self.accept()

    def click_cancel(self):
        self.reject()