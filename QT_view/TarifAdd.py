from PyQt5.QtWidgets import QDialog

from Repository.Rep_Tarif import TarifRepository

from QT_view.TarifAddWin import Ui_TarifAdd

class TarifAddDialog(QDialog):
    def __init__(self, tarif_rep: TarifRepository):
        super(TarifAddDialog, self).__init__()
        self.tarif_rep = tarif_rep
        self.tarif_d = tarif_rep.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_TarifAdd()
        self.ui.setupUi(self)

        if (len(self.tarif_d['tarif_name'])):
            self.ui.lineEdit_tarif_name.setText(self.tarif_d['tarif_name'])

        if (len(self.tarif_d['another_minute'])):
            self.ui.lineEdit_another_minute.setText(self.tarif_d['another_minute'])

        if (len(self.tarif_d['home_minute'])):
            self.ui.lineEdit_home_minute.setText(self.tarif_d['home_minute'])

        if (len(self.tarif_d['sms'])):
            self.ui.lineEdit_sms.setText(self.tarif_d['sms'])

        if (len(self.tarif_d['internet'])):
            self.ui.lineEdit_internet.setText(self.tarif_d['internet'])

        if (len(self.tarif_d['speed_internet'])):
            self.ui.lineEdit_speed_internet.setText(self.tarif_d['speed_internet'])

        if (len(self.tarif_d['cost'])):
            self.ui.lineEdit_cost.setText(self.tarif_d['cost'])

        if (len(self.tarif_d['translate_number'])):
            self.ui.lineEdit_translate_number.setText(self.tarif_d['translate_number'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        t_tarif_name = self.ui.lineEdit_tarif_name.text()
        t_tarif_name = t_tarif_name.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        t_another_minute = self.ui.lineEdit_another_minute.text()
        t_another_minute = t_another_minute.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        t_home_minute = self.ui.lineEdit_home_minute.text()
        t_home_minute = t_home_minute.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        t_sms = self.ui.lineEdit_sms.text()
        t_sms = t_sms.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        t_internet = self.ui.lineEdit_internet.text()
        t_internet = t_internet.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        t_speed_internet = self.ui.lineEdit_speed_internet.text()
        t_speed_internet = t_speed_internet.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        t_cost = self.ui.lineEdit_cost.text()
        t_cost = t_cost.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        t_traslate_number = self.ui.lineEdit_translate_number.text()
        t_traslate_number = t_traslate_number.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.tarif_d['id'] == -1):
            if (len(t_tarif_name)):
                self.tarif_d['tarif_name'] = t_tarif_name
                self.tarif_d['another_minute'] = t_another_minute
                self.tarif_d['home_minute'] = t_home_minute
                self.tarif_d['sms'] = t_sms
                self.tarif_d['internet'] = t_internet
                self.tarif_d['speed_internet'] = t_speed_internet
                self.tarif_d['cost'] = t_cost
                self.tarif_d['traslate_number'] = t_traslate_number
                self.tarif_d['id'] = self.tarif_rep.new_tarif(self.tarif_d)
                self.tarif_rep.set_dict(self.tarif_d)
                self.accept()
        else:
            if (len(t_tarif_name)):
                self.tarif_d['tarif_name'] = t_tarif_name
                self.tarif_d['another_minute'] = t_another_minute
                self.tarif_d['home_minute'] = t_home_minute
                self.tarif_d['sms'] = t_sms
                self.tarif_d['internet'] = t_internet
                self.tarif_d['speed_internet'] = t_speed_internet
                self.tarif_d['cost'] = t_cost
                self.tarif_d['traslate_number'] = t_traslate_number
                self.tarif_rep.update_tarif(self.tarif_d)
                self.tarif_rep.set_dict(self.tarif_d)
                self.accept()

    def click_cancel(self):
        self.reject()