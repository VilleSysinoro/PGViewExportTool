# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportTool.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dbSettingsFrame = QFrame(self.centralwidget)
        self.dbSettingsFrame.setObjectName(u"dbSettingsFrame")
        self.dbSettingsFrame.setGeometry(QRect(20, 30, 481, 201))
        self.dbSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dbSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.dbSettingsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.passwordLabel = QLabel(self.dbSettingsFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")
        font = QFont()
        font.setPointSize(11)
        self.passwordLabel.setFont(font)

        self.gridLayout.addWidget(self.passwordLabel, 4, 0, 1, 1)

        self.portLabel = QLabel(self.dbSettingsFrame)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font)

        self.gridLayout.addWidget(self.portLabel, 1, 0, 1, 1)

        self.databaseLabel = QLabel(self.dbSettingsFrame)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font)

        self.gridLayout.addWidget(self.databaseLabel, 2, 0, 1, 1)

        self.serverLineEdit = QLineEdit(self.dbSettingsFrame)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        self.serverLineEdit.setFont(font)

        self.gridLayout.addWidget(self.serverLineEdit, 0, 1, 1, 1)

        self.portLineEdit = QLineEdit(self.dbSettingsFrame)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font)

        self.gridLayout.addWidget(self.portLineEdit, 1, 1, 1, 1)

        self.userNameLabel = QLabel(self.dbSettingsFrame)
        self.userNameLabel.setObjectName(u"userNameLabel")
        self.userNameLabel.setFont(font)

        self.gridLayout.addWidget(self.userNameLabel, 3, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(self.dbSettingsFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setFont(font)

        self.gridLayout.addWidget(self.passwordLineEdit, 4, 1, 1, 1)

        self.serverLabel = QLabel(self.dbSettingsFrame)
        self.serverLabel.setObjectName(u"serverLabel")
        self.serverLabel.setFont(font)

        self.gridLayout.addWidget(self.serverLabel, 0, 0, 1, 1)

        self.databaseLineEdit = QLineEdit(self.dbSettingsFrame)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setFont(font)

        self.gridLayout.addWidget(self.databaseLineEdit, 2, 1, 1, 1)

        self.userNameLineEdit = QLineEdit(self.dbSettingsFrame)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")
        self.userNameLineEdit.setFont(font)

        self.gridLayout.addWidget(self.userNameLineEdit, 3, 1, 1, 1)

        self.testConnectionPushButton = QPushButton(self.dbSettingsFrame)
        self.testConnectionPushButton.setObjectName(u"testConnectionPushButton")
        self.testConnectionPushButton.setFont(font)
        self.testConnectionPushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.testConnectionPushButton, 5, 0, 1, 1)

        self.dbSettingsLabel = QLabel(self.centralwidget)
        self.dbSettingsLabel.setObjectName(u"dbSettingsLabel")
        self.dbSettingsLabel.setGeometry(QRect(20, 10, 211, 16))
        self.dbSettingsLabel.setFont(font)
        self.viewNameLineEdit = QLineEdit(self.centralwidget)
        self.viewNameLineEdit.setObjectName(u"viewNameLineEdit")
        self.viewNameLineEdit.setGeometry(QRect(20, 282, 361, 22))
        self.viewNameLineEdit.setFont(font)
        self.viewNameLabel = QLabel(self.centralwidget)
        self.viewNameLabel.setObjectName(u"viewNameLabel")
        self.viewNameLabel.setGeometry(QRect(20, 252, 101, 16))
        self.viewNameLabel.setFont(font)
        self.exportPushButton = QPushButton(self.centralwidget)
        self.exportPushButton.setObjectName(u"exportPushButton")
        self.exportPushButton.setGeometry(QRect(540, 280, 111, 24))
        self.exportPushButton.setFont(font)
        self.exportPushButton.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.previewTableWidget = QTableWidget(self.centralwidget)
        self.previewTableWidget.setObjectName(u"previewTableWidget")
        self.previewTableWidget.setGeometry(QRect(20, 340, 751, 191))
        self.getDataPushButton = QPushButton(self.centralwidget)
        self.getDataPushButton.setObjectName(u"getDataPushButton")
        self.getDataPushButton.setGeometry(QRect(410, 280, 111, 24))
        self.getDataPushButton.setFont(font)
        self.getDataPushButton.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.previewLabel = QLabel(self.centralwidget)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setGeometry(QRect(20, 320, 211, 16))
        self.previewLabel.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuOhje = QMenu(self.menubar)
        self.menuOhje.setObjectName(u"menuOhje")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOhje.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.serverLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Palvelimen nimi tai IP-osoite", None))
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TCP-portin numero, oletus 5432", None))
        self.userNameLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4n salasana", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.databaseLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tietokannan nimi, hallintatietokanta postgres", None))
        self.userNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus, oletusp\u00e4\u00e4k\u00e4ytt\u00e4j\u00e4 postgres", None))
        self.testConnectionPushButton.setText(QCoreApplication.translate("MainWindow", u"Testaa yhteys", None))
        self.dbSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokantayhteyden asetukset", None))
        self.viewNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tietokannan n\u00e4kym\u00e4n nimi, jonka tiedot vied\u00e4\u00e4n", None))
        self.viewNameLabel.setText(QCoreApplication.translate("MainWindow", u"N\u00e4kym\u00e4n nimi", None))
        self.exportPushButton.setText(QCoreApplication.translate("MainWindow", u"Vie tiedostoon", None))
        self.getDataPushButton.setText(QCoreApplication.translate("MainWindow", u"Hae", None))
        self.previewLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.menuOhje.setTitle(QCoreApplication.translate("MainWindow", u"Ohje", None))
    # retranslateUi

