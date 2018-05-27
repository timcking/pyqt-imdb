from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap, QImage
import urllib
from ui_castdialog import Ui_CastDialog
from TriviaApp import TriviaDialog
from MovieData import MovieData
# from MovieBrowserApp import MovieDialog

class CastDialog(QDialog):
    m_person_id = None
    m_parent = None
    movieData = MovieData()

    def __init__(self, parent, person_id):
        super(CastDialog, self).__init__(parent)

        # Set up the user interface from Designer.
        self.cast = Ui_CastDialog()
        self.resize(800, 625)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.cast.setupUi(self)

        # Connect up the buttons and widgets
        self.cast.buttonClose.clicked.connect(self.onCloseClick)
        self.cast.buttonTrivia.clicked.connect(self.onTriviaClick)
        self.cast.listMovies.clicked.connect(self.onMovieClick)

        self.m_person_id = person_id
        # ToDo, use m_parent to call MovieDialog
        self.m_parent = parent

        self.getActorInfo()
        self.getMovieInfo()

        QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

    def getMovieInfo(self):
        person = self.movieData.get_person_data(self.m_person_id)
        s_result = person.get_titlesRefs()
        tk = person.get

        count = 0
        try:
            for item in s_result:
                # The first movie is always 1939, so ignore first
                # ToDo, better way to do this
                if count > 0:
                    self.cast.listMovies.addItem(item)
                count += 1

        except KeyError:
            pass

    def getActorInfo(self):
        s_result = self.movieData.get_person_data(self.m_person_id)

        self.cast.labelName.setText(s_result['name'])

        try:
            self.cast.leDeath.setText(s_result['death date'])
        except KeyError:
            pass

        try:
            self.cast.leBirth.setText('%s, %s' % (s_result['birth date'], s_result['birth info']['birth place']))
        except KeyError:
            pass

        try:
            url = str(s_result['headshot'])
            img = QImage()
            data = urllib.request.urlopen(url).read()
            img.loadFromData(data)
            self.cast.labelPhoto.setPixmap(QPixmap(img).scaledToWidth(100))

        except KeyError:
            pass

    def onMovieClick(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        cur_row = self.cast.listMovies.currentRow()
        movieTitle = (self.cast.listMovies.currentItem().text())
        print(movieTitle)


        self.m_parent.clearText()
        self.m_parent.fillMovieList(movieTitle)

        QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)
        self.close()

    def onTriviaClick(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.triv = TriviaDialog(self.m_person_id)
        self.triv.exec_()

    def onCloseClick(self):
        self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dialog = CastDialog(1234)
    sys.exit(dialog.exec_())
