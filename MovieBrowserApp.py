from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
from ui_moviedialog import Ui_MovieDialog
from CastApp import CastDialog
from MovieData import MovieData

class MovieDialog(QDialog):
    dictMovie = {}
    dictCast = {}
    movieData = MovieData()

    def __init__(self, *positional_parameters, **keyword_parameters):
        super(MovieDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MovieDialog()
        self.resize(800, 625)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.ui.setupUi(self)

        # Connect up the buttons and widgets
        self.ui.buttonExit.clicked.connect(self.onExitClick)
        self.ui.buttonSearch.clicked.connect(self.onSearchClick)

        self.ui.listMovie.clicked.connect(self.onMovieClick)
        self.ui.listCast.clicked.connect(self.onCastClick)

        if ('optional' in keyword_parameters):
            self.fillMovieList(keyword_parameters['optional'])
        
    def fillMovieList(self, title):
        s_result = self.movieData.search_movie_data(title)

        index_count = 0
        for item in s_result:
            self.ui.listMovie.addItem(item['long imdb canonical title'])
            self.dictMovie[index_count] = item.movieID
            index_count += 1

    def clearText(self):
        self.ui.leSearch.setText("")
        self.ui.listMovie.clear()
        self.ui.listCast.clear()
        self.ui.leDirector.setText("")
        self.ui.tePlot.setPlainText("")
        self.ui.leRuntime.setText("")

    def onCastClick(self):
        cur_row = self.ui.listCast.currentRow()
        personName = (self.ui.listCast.currentItem().text())
        person_id = self.dictCast[cur_row]

        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.cast = CastDialog(self, person_id)
        self.cast.exec_()

    def onMovieClick(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        self.ui.listCast.clear()

        cur_row = self.ui.listMovie.currentRow()
        movieTitle = (self.ui.listMovie.currentItem().text())
        movie_id = self.dictMovie[cur_row]

        s_result = self.movieData.get_movie_data(movie_id)

        try:
            index_count = 0
            for person in s_result['cast']:
                self.dictCast[index_count] = person.personID
                self.ui.listCast.addItem(str(person))
                index_count += 1
        except KeyError:
            print("Cast data not found")

        try:
            self.ui.leDirector.setText(str(s_result['director'][0]))
            self.ui.tePlot.setPlainText(str(s_result['plot outline']))
            self.ui.leRuntime.setText(str(s_result['runtimes'][0]))
        except KeyError:
            pass

        QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

    def onSearchClick(self):
        if len(self.ui.leSearch.text()) > 0:
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

            title = self.ui.leSearch.text()
            self.clearText()
            self.fillMovieList(title)

            QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor)

    def onExitClick(self):
        sys.exit(0)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # dialog = MovieDialog(optional="Casablanca")
    dialog = MovieDialog()
    sys.exit(dialog.exec_())
