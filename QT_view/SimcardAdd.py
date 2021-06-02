from PyQt5.QtWidgets import QDialog

from Repository.Rep_SimCard import SimCardRepository

from QT_view.SimcardAddWin import Ui_SimcardAdd

class SimcardAddDialog(QDialog):
    def __init__(self,  simcard_rep: SimCardRepository):
        super(SimcardAddDialog, self).__init__()
        self.simcard_rep = simcard_rep
        self.simcard_d = simcard_rep.get_dict()
        self.initUI()

    def initUI(self):
        self.ui = Ui_SimcardAdd()
        self.ui.setupUi(self)

        if (len(self.simcard_d['ICCIM'])):
            self.ui.lineEdit_ICCIM.setText(self.simcard_d['ICCIM'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        s_iccim = self.ui.lineEdit_ICCIM.text()
        s_iccim = s_iccim.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.simcard_d['id'] == -1):
            if (len(s_iccim)):
                self.simcard_d['ICCIM'] = s_iccim
                self.simcard_d['id'] = self.simcard_rep.new_simcard(self.simcard_d)
                self.simcard_rep.set_dict(self.simcard_d)
                self.accept()
        else:
            if (len(s_iccim)):
                self.simcard_d['ICCIM'] = s_iccim
                self.simcard_rep.update_simcard(self.simcard_d)
                self.simcard_rep.set_dict(self.simcard_d)
                self.accept()

    def click_cancel(self):
        self.reject()