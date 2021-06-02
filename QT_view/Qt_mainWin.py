import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from QT_view.PassportDialog import PassportQt
from QT_view.CityDialog import CityQt
from QT_view.AddressWin import AddressQt
from QT_view.AbonentDialog import AbonentQt
from QT_view.ContractWin import ContractQt
from QT_view.SimcardWin import SimcardQt
from QT_view.PhoneWin import PhoneQt
from QT_view.ChangelogWin import ChangelogQt
from QT_view.TarifWin import TarifQt
from QT_view.Qt_Main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(231, 365)

        self.ui.pushButton_2.clicked.connect(self.click_type_passport)
        self.ui.pushButton_3.clicked.connect(self.click_type_city)
        self.ui.pushButton_4.clicked.connect(self.click_type_address)
        self.ui.pushButton_5.clicked.connect(self.click_type_abonent)
        self.ui.pushButton_6.clicked.connect(self.click_type_contract)
        self.ui.pushButton_7.clicked.connect(self.click_type_simcard)
        self.ui.pushButton_8.clicked.connect(self.click_type_phonenumber)
        self.ui.pushButton_9.clicked.connect(self.click_type_tarif)
        self.ui.pushButton_10.clicked.connect(self.click_type_changelog)



    def click_type_passport(self):
        passport_dialog = PassportQt()
        passport_dialog.exec()

    def click_type_city(self):
        city_dialog = CityQt()
        city_dialog.exec()

    def click_type_address(self):
        address_dialog = AddressQt()
        address_dialog.exec()

    def click_type_abonent(self):
        abonent_dialog = AbonentQt()
        abonent_dialog.exec()

    def click_type_contract(self):
        contract_dialog = ContractQt()
        contract_dialog.exec()

    def click_type_simcard(self):
        simcard_dialog = SimcardQt()
        simcard_dialog.exec()

    def click_type_phonenumber(self):
        phone_number_dialog = PhoneQt()
        phone_number_dialog.exec()

    def click_type_tarif(self):
        tarif_dialog = TarifQt()
        tarif_dialog.exec()

    def click_type_changelog(self):
        changelog_dialog = ChangelogQt()
        changelog_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWin = MainWindow()
    MainWin.show()
    sys.exit(app.exec_())