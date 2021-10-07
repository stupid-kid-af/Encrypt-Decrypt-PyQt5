# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(450, 450)
        Window.setMinimumSize(QtCore.QSize(450, 450))
        Window.setMaximumSize(QtCore.QSize(450, 450))
        Window.setStyleSheet("background-color: rgb(14, 22, 33);")
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.DragDrop = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DragDrop.sizePolicy().hasHeightForWidth())
        self.DragDrop.setSizePolicy(sizePolicy)
        self.DragDrop.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.DragDrop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DragDrop.setStyleSheet("background-color: rgb(24, 37, 51);\n"
"color: rgb(238, 238, 236);\n"
"padding: 15px;")
        self.DragDrop.setAlignment(QtCore.Qt.AlignCenter)
        self.DragDrop.setDragEnabled(True)
        self.DragDrop.setReadOnly(False)
        self.DragDrop.setObjectName("DragDrop")
        self.gridLayout.addWidget(self.DragDrop, 0, 0, 1, 3)
        self.passphrase = QtWidgets.QLineEdit(self.centralwidget)
        self.passphrase.setMinimumSize(QtCore.QSize(0, 45))
        self.passphrase.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.passphrase.setAcceptDrops(False)
        self.passphrase.setStyleSheet("background-color: rgb(24, 37, 51);\n"
"color: rgb(238, 238, 236);\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"")
        self.passphrase.setInputMask("")
        self.passphrase.setText("")
        self.passphrase.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passphrase.setObjectName("passphrase")
        self.gridLayout.addWidget(self.passphrase, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setMinimumSize(QtCore.QSize(180, 50))
        self.encryptBtn.setMaximumSize(QtCore.QSize(3000, 50))
        self.encryptBtn.setAutoFillBackground(False)
        self.encryptBtn.setStyleSheet("#encryptBtn {\n"
"outline: 0;\n"
"border: 0;\n"
"background-color: rgb(14, 22, 33);\n"
"color: rgb(106, 179, 243);\n"
"text-transform: uppercase;\n"
"}\n"
"\n"
"#encryptBtn:hover {\n"
"background-color: rgb(24, 37, 51);\n"
"}")
        self.encryptBtn.setAutoDefault(False)
        self.encryptBtn.setDefault(False)
        self.encryptBtn.setFlat(False)
        self.encryptBtn.setObjectName("encryptBtn")
        self.horizontalLayout.addWidget(self.encryptBtn)
        self.decryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decryptBtn.setMinimumSize(QtCore.QSize(180, 50))
        self.decryptBtn.setMaximumSize(QtCore.QSize(3000, 50))
        self.decryptBtn.setStyleSheet("#decryptBtn {\n"
"outline: 0;\n"
"border: 0;\n"
"background-color: rgb(14, 22, 33);\n"
"color: rgb(106, 179, 243);\n"
"text-transform: uppercase;\n"
"}\n"
"\n"
"#decryptBtn:hover {\n"
"background-color: rgb(24, 37, 51);\n"
"}")
        self.decryptBtn.setFlat(False)
        self.decryptBtn.setObjectName("decryptBtn")
        self.horizontalLayout.addWidget(self.decryptBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 8, 1, 1, 1)
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
        Window.setTabOrder(self.passphrase, self.decryptBtn)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "File encryption"))
        self.DragDrop.setPlaceholderText(_translate("Window", "Drag & drop here"))
        self.passphrase.setPlaceholderText(_translate("Window", "Passphrase"))
        self.encryptBtn.setText(_translate("Window", "Encrypt"))
        self.decryptBtn.setText(_translate("Window", "Decrypt"))

