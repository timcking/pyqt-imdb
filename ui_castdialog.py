# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_castdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CastDialog(object):
    def setupUi(self, CastDialog):
        CastDialog.setObjectName("CastDialog")
        CastDialog.resize(715, 543)
        CastDialog.setMinimumSize(QtCore.QSize(520, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("film.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CastDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(CastDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelName = QtWidgets.QLabel(CastDialog)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout.addWidget(self.labelName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelPhoto = QtWidgets.QLabel(CastDialog)
        self.labelPhoto.setText("")
        self.labelPhoto.setObjectName("labelPhoto")
        self.horizontalLayout.addWidget(self.labelPhoto)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtWidgets.QLabel(CastDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leBirth = QtWidgets.QLineEdit(CastDialog)
        self.leBirth.setObjectName("leBirth")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leBirth)
        self.label_4 = QtWidgets.QLabel(CastDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.leDeath = QtWidgets.QLineEdit(CastDialog)
        self.leDeath.setObjectName("leDeath")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leDeath)
        self.label_2 = QtWidgets.QLabel(CastDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.listTrivia = QtWidgets.QListWidget(CastDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listTrivia.sizePolicy().hasHeightForWidth())
        self.listTrivia.setSizePolicy(sizePolicy)
        self.listTrivia.setObjectName("listTrivia")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.listTrivia)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CastDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CastDialog)
        self.buttonBox.accepted.connect(CastDialog.accept)
        self.buttonBox.rejected.connect(CastDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CastDialog)
        CastDialog.setTabOrder(self.leBirth, self.leDeath)

    def retranslateUi(self, CastDialog):
        _translate = QtCore.QCoreApplication.translate
        CastDialog.setWindowTitle(_translate("CastDialog", "Cast Information"))
        self.labelName.setText(_translate("CastDialog", "Actor Name"))
        self.label.setText(_translate("CastDialog", "Birth"))
        self.label_4.setText(_translate("CastDialog", "Death"))
        self.label_2.setText(_translate("CastDialog", "Trivia"))

