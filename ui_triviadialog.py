# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_triviadialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TriviaDialog(object):
    def setupUi(self, TriviaDialog):
        TriviaDialog.setObjectName("TriviaDialog")
        TriviaDialog.resize(650, 497)
        self.verticalLayout = QtWidgets.QVBoxLayout(TriviaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(TriviaDialog)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.listTrivia = QtWidgets.QListWidget(TriviaDialog)
        self.listTrivia.setObjectName("listTrivia")
        self.verticalLayout.addWidget(self.listTrivia)
        self.buttonBox = QtWidgets.QDialogButtonBox(TriviaDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TriviaDialog)
        self.buttonBox.accepted.connect(TriviaDialog.accept)
        self.buttonBox.rejected.connect(TriviaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TriviaDialog)

    def retranslateUi(self, TriviaDialog):
        _translate = QtCore.QCoreApplication.translate
        TriviaDialog.setWindowTitle(_translate("TriviaDialog", "Trivia"))
        self.labelName.setText(_translate("TriviaDialog", "Actor Name"))

