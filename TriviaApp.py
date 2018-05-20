from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
from ui_triviadialog import Ui_TriviaDialog
from MovieData import MovieData

class TriviaDialog(QDialog):
    def __init__(self, person_id):
        super(TriviaDialog, self).__init__()

        # Set up the user interface from Designer.
        self.triv = Ui_TriviaDialog()
        self.resize(800, 625)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.triv.setupUi(self)

        self.getTrivia(person_id)

    def getTrivia(self, person_id):
        movieData = MovieData()
        s_result = movieData.get_person_data(person_id)

        self.triv.labelName.setText(s_result['name'])

        try:
            for item in s_result['trivia']:
                self.triv.listTrivia.addItem(item)
        except KeyError:
            pass

        QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dialog = TriviaDialog('0000007')
    sys.exit(dialog.exec_())
