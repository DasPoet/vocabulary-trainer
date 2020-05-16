# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vocabulary_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Vokabeltrainer(object):
    def setupUi(self, Vokabeltrainer):
        Vokabeltrainer.setObjectName("Vokabeltrainer")
        Vokabeltrainer.resize(570, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Vokabeltrainer.sizePolicy().hasHeightForWidth())
        Vokabeltrainer.setSizePolicy(sizePolicy)
        Vokabeltrainer.setMinimumSize(QtCore.QSize(570, 350))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Vokabeltrainer.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Vokabeltrainer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy)
        self.downloadButton.setMinimumSize(QtCore.QSize(55, 20))
        self.downloadButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon)
        self.downloadButton.setIconSize(QtCore.QSize(48, 48))
        self.downloadButton.setObjectName("downloadButton")
        self.gridLayout.addWidget(self.downloadButton, 10, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 10, 1, 1)
        self.entryInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entryInput.sizePolicy().hasHeightForWidth())
        self.entryInput.setSizePolicy(sizePolicy)
        self.entryInput.setMinimumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entryInput.setFont(font)
        self.entryInput.setObjectName("entryInput")
        self.gridLayout.addWidget(self.entryInput, 4, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 11, 1, 1)
        self.soundButtonRight = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soundButtonRight.sizePolicy().hasHeightForWidth())
        self.soundButtonRight.setSizePolicy(sizePolicy)
        self.soundButtonRight.setMinimumSize(QtCore.QSize(40, 25))
        self.soundButtonRight.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/sound_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soundButtonRight.setIcon(icon1)
        self.soundButtonRight.setIconSize(QtCore.QSize(32, 32))
        self.soundButtonRight.setObjectName("soundButtonRight")
        self.gridLayout.addWidget(self.soundButtonRight, 6, 9, 1, 1)
        self.labelScore = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelScore.sizePolicy().hasHeightForWidth())
        self.labelScore.setSizePolicy(sizePolicy)
        self.labelScore.setMinimumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelScore.setFont(font)
        self.labelScore.setObjectName("labelScore")
        self.gridLayout.addWidget(self.labelScore, 10, 9, 1, 1)
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOutput.sizePolicy().hasHeightForWidth())
        self.labelOutput.setSizePolicy(sizePolicy)
        self.labelOutput.setMinimumSize(QtCore.QSize(170, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelOutput.setFont(font)
        self.labelOutput.setText("")
        self.labelOutput.setTextFormat(QtCore.Qt.RichText)
        self.labelOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutput.setObjectName("labelOutput")
        self.gridLayout.addWidget(self.labelOutput, 4, 8, 1, 3)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(55, 20))
        self.deleteButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setIconSize(QtCore.QSize(32, 32))
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 10, 1, 1, 1)
        self.modeButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeButton.sizePolicy().hasHeightForWidth())
        self.modeButton.setSizePolicy(sizePolicy)
        self.modeButton.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.modeButton.setFont(font)
        self.modeButton.setObjectName("modeButton")
        self.gridLayout.addWidget(self.modeButton, 8, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem5, 11, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem6, 7, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(5, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem7, 9, 6, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem8, 5, 0, 1, 1)
        self.buttonCheck = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCheck.sizePolicy().hasHeightForWidth())
        self.buttonCheck.setSizePolicy(sizePolicy)
        self.buttonCheck.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonCheck.setFont(font)
        self.buttonCheck.setObjectName("buttonCheck")
        self.gridLayout.addWidget(self.buttonCheck, 8, 6, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 6, 1, 3)
        self.soundButtonLeft = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soundButtonLeft.sizePolicy().hasHeightForWidth())
        self.soundButtonLeft.setSizePolicy(sizePolicy)
        self.soundButtonLeft.setMinimumSize(QtCore.QSize(30, 25))
        self.soundButtonLeft.setText("")
        self.soundButtonLeft.setIcon(icon1)
        self.soundButtonLeft.setIconSize(QtCore.QSize(32, 32))
        self.soundButtonLeft.setObjectName("soundButtonLeft")
        self.gridLayout.addWidget(self.soundButtonLeft, 6, 2, 1, 1)
        self.labelLeft = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLeft.sizePolicy().hasHeightForWidth())
        self.labelLeft.setSizePolicy(sizePolicy)
        self.labelLeft.setMinimumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelLeft.setFont(font)
        self.labelLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLeft.setObjectName("labelLeft")
        self.gridLayout.addWidget(self.labelLeft, 2, 1, 1, 3)
        self.labelRight = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRight.sizePolicy().hasHeightForWidth())
        self.labelRight.setSizePolicy(sizePolicy)
        self.labelRight.setMinimumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelRight.setFont(font)
        self.labelRight.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRight.setObjectName("labelRight")
        self.gridLayout.addWidget(self.labelRight, 2, 8, 1, 3)
        Vokabeltrainer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Vokabeltrainer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menubar.setObjectName("menubar")
        self.miscellaneous_menu = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miscellaneous_menu.sizePolicy().hasHeightForWidth())
        self.miscellaneous_menu.setSizePolicy(sizePolicy)
        self.miscellaneous_menu.setObjectName("miscellaneous_menu")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_menu.sizePolicy().hasHeightForWidth())
        self.file_menu.setSizePolicy(sizePolicy)
        self.file_menu.setObjectName("file_menu")
        Vokabeltrainer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Vokabeltrainer)
        self.statusbar.setObjectName("statusbar")
        Vokabeltrainer.setStatusBar(self.statusbar)
        self.actionvocabulary = QtWidgets.QAction(Vokabeltrainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionvocabulary.setFont(font)
        self.actionvocabulary.setObjectName("actionvocabulary")
        self.actiongrammar = QtWidgets.QAction(Vokabeltrainer)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actiongrammar.setFont(font)
        self.actiongrammar.setObjectName("actiongrammar")
        self.settingsLabel = QtWidgets.QAction(Vokabeltrainer)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsLabel.setIcon(icon3)
        self.settingsLabel.setObjectName("settingsLabel")
        self.editLabel = QtWidgets.QAction(Vokabeltrainer)
        self.editLabel.setObjectName("editLabel")
        self.actionDownload_sound_files = QtWidgets.QAction(Vokabeltrainer)
        self.actionDownload_sound_files.setObjectName("actionDownload_sound_files")
        self.actionDelete_sound_files = QtWidgets.QAction(Vokabeltrainer)
        self.actionDelete_sound_files.setObjectName("actionDelete_sound_files")
        self.downloadLabel = QtWidgets.QAction(Vokabeltrainer)
        self.downloadLabel.setObjectName("downloadLabel")
        self.deleteLabel = QtWidgets.QAction(Vokabeltrainer)
        self.deleteLabel.setIcon(icon2)
        self.deleteLabel.setObjectName("deleteLabel")
        self.save_as_pdf_label = QtWidgets.QAction(Vokabeltrainer)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_as_pdf_label.setIcon(icon4)
        self.save_as_pdf_label.setObjectName("save_as_pdf_label")
        self.miscellaneous_menu.addAction(self.settingsLabel)
        self.miscellaneous_menu.addAction(self.editLabel)
        self.file_menu.addAction(self.downloadLabel)
        self.file_menu.addAction(self.deleteLabel)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.save_as_pdf_label)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.miscellaneous_menu.menuAction())

        self.retranslateUi(Vokabeltrainer)
        QtCore.QMetaObject.connectSlotsByName(Vokabeltrainer)

    def retranslateUi(self, Vokabeltrainer):
        _translate = QtCore.QCoreApplication.translate
        Vokabeltrainer.setWindowTitle(_translate("Vokabeltrainer", "Vokabeltrainer by @DasPoet"))
        self.downloadButton.setToolTip(_translate("Vokabeltrainer", "Download all sound files"))
        self.labelScore.setText(_translate("Vokabeltrainer", "Score: "))
        self.deleteButton.setToolTip(_translate("Vokabeltrainer", "Delete all sound files"))
        self.modeButton.setText(_translate("Vokabeltrainer", "random mode"))
        self.buttonCheck.setText(_translate("Vokabeltrainer", "Check"))
        self.labelLeft.setText(_translate("Vokabeltrainer", "Deutsch"))
        self.labelRight.setText(_translate("Vokabeltrainer", "English"))
        self.miscellaneous_menu.setTitle(_translate("Vokabeltrainer", "Miscellaneous"))
        self.file_menu.setTitle(_translate("Vokabeltrainer", "File"))
        self.actionvocabulary.setText(_translate("Vokabeltrainer", "vocabulary"))
        self.actiongrammar.setText(_translate("Vokabeltrainer", "grammar"))
        self.settingsLabel.setText(_translate("Vokabeltrainer", "Settings"))
        self.editLabel.setText(_translate("Vokabeltrainer", "Editor"))
        self.actionDownload_sound_files.setText(_translate("Vokabeltrainer", "Download sound files"))
        self.actionDelete_sound_files.setText(_translate("Vokabeltrainer", "Delete sound files"))
        self.downloadLabel.setText(_translate("Vokabeltrainer", "Download all sounds"))
        self.deleteLabel.setText(_translate("Vokabeltrainer", "Delete all sounds"))
        self.save_as_pdf_label.setText(_translate("Vokabeltrainer", "Save as .pdf"))
