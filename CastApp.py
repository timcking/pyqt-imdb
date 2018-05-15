from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
from ui_castdialog import Ui_CastDialog
from MovieData import MovieData

class CastDialog(QDialog):
    def __init__(self, person_id):
        super(CastDialog, self).__init__()

        # Set up the user interface from Designer.
        self.cast = Ui_CastDialog()
        self.cast.setupUi(self)

        # Connect up the buttons and widgets
        self.cast.buttonBox.rejected.connect(self.reject)

        self.getActorInfo(person_id)

    def getActorInfo(self, person_id):
        movieData = MovieData()
        s_result = movieData.get_person_data(person_id)

        self.cast.labelName.setText(s_result['name'])

        try:
            self.cast.leDeath.setText(s_result['death date'])
        except KeyError:
            pass

        try:
            self.cast.leBirth.setText('%s, %s' % (s_result['birth date'], s_result['birth info']['birth place']))
        except KeyError:
            print("Actor data not found")

        try:
            self.cast.labelURL.setOpenExternalLinks(True)
            urlHead = """<html><head/><body><p><a href=\""""
            urlTail = """"><span style=\\" text-decoration: underline; color:#0000ff;\\">Link to Photo</span></a></p></body></html>"""
            url = s_result['headshot']

            stringUrl = urlHead.replace("\n", "") + url.replace("\n", "") + urlTail.replace("\n", "")

            self.cast.labelURL.setText(stringUrl)

        except KeyError:
            pass

        try:
            for item in s_result['trivia']:
                self.cast.listTrivia.addItem(item)
        except KeyError:
            pass

        QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dialog = CastDialog(1234)
    sys.exit(dialog.exec_())
