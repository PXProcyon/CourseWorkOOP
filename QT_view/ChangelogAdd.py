from PyQt5.QtWidgets import QDialog

from Repository.Rep_Changelog import ChangelogRepository

from QT_view.ChangelogAddWin import Ui_ChangelogAdd

class ChangelogAddDialog(QDialog):
    def __init__(self, changelog_rep: ChangelogRepository):
        super(ChangelogAddDialog, self).__init__()
        self.changelog_rep = changelog_rep
        self.changelog_d = changelog_rep.get_dict()
        self.initUI()
    def initUI(self):
        self.ui = Ui_ChangelogAdd()
        self.ui.setupUi(self)

        if (len(self.changelog_d['data_change'])):
            self.ui.lineEdit_data_change.setText(self.changelog_d['data_change'])

        if (len(self.changelog_d['content'])):
            self.ui.lineEdit_content.setText(self.changelog_d['content'])

        self.ui.pushButton.clicked.connect(self.click_ok)
        self.ui.pushButton_2.clicked.connect(self.click_cancel)

    def click_ok(self):
        cha_data_change = self.ui.lineEdit_data_change.text()
        cha_data_change = cha_data_change.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")
        cha_content = self.ui.lineEdit_content.text()
        cha_content = cha_content.strip(" _,./-=)(*&?^%$#@!\"№;%:?}{][':<>\n\r\t\v")

        if (self.changelog_d['id'] == -1):
            if (len(cha_data_change)):
                self.changelog_d['data_change'] = cha_data_change
                self.changelog_d['content'] = cha_content
                self.changelog_d['id'] = self.changelog_rep.new_changelog(self.changelog_d)
                self.changelog_rep.set_dict(self.changelog_d)
                self.accept()
        else:
            if (len(cha_data_change)):
                self.changelog_d['data_change'] = cha_data_change
                self.changelog_d['content'] = cha_content
                self.changelog_rep.update_changelog(self.changelog_d)
                self.changelog_rep.set_dict(self.changelog_d)
                self.accept()



    def click_cancel(self):
        self.reject()