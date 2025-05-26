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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(952, 696)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.separatorGroupBox = QGroupBox(self.centralwidget)
        self.separatorGroupBox.setObjectName(u"separatorGroupBox")
        self.separatorGroupBox.setGeometry(QRect(530, 20, 191, 221))
        self.separatorGroupBox.setFont(font)
        self.semicolonRadioButton = QRadioButton(self.separatorGroupBox)
        self.semicolonRadioButton.setObjectName(u"semicolonRadioButton")
        self.semicolonRadioButton.setGeometry(QRect(10, 30, 111, 26))
        self.semicolonRadioButton.setFont(font)
        self.semicolonRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.semicolonRadioButton.setCheckable(True)
        self.semicolonRadioButton.setChecked(False)
        self.commaRadioButton = QRadioButton(self.separatorGroupBox)
        self.commaRadioButton.setObjectName(u"commaRadioButton")
        self.commaRadioButton.setGeometry(QRect(10, 80, 109, 26))
        self.commaRadioButton.setFont(font)
        self.commaRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabRadioButton = QRadioButton(self.separatorGroupBox)
        self.tabRadioButton.setObjectName(u"tabRadioButton")
        self.tabRadioButton.setGeometry(QRect(10, 130, 74, 26))
        self.tabRadioButton.setFont(font)
        self.tabRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.otherSeparatorRadioButton = QRadioButton(self.separatorGroupBox)
        self.otherSeparatorRadioButton.setObjectName(u"otherSeparatorRadioButton")
        self.otherSeparatorRadioButton.setGeometry(QRect(10, 182, 55, 26))
        self.otherSeparatorRadioButton.setFont(font)
        self.otherSeparatorRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.separatorLineEdit = QLineEdit(self.separatorGroupBox)
        self.separatorLineEdit.setObjectName(u"separatorLineEdit")
        self.separatorLineEdit.setGeometry(QRect(70, 180, 31, 26))
        self.separatorLineEdit.setFont(font)
        self.objectTypeLabel = QLabel(self.centralwidget)
        self.objectTypeLabel.setObjectName(u"objectTypeLabel")
        self.objectTypeLabel.setGeometry(QRect(310, 290, 107, 20))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.objectTypeLabel.setFont(font1)
        self.objectNameComboBox = QComboBox(self.centralwidget)
        self.objectNameComboBox.setObjectName(u"objectNameComboBox")
        self.objectNameComboBox.setGeometry(QRect(490, 310, 311, 26))
        self.objectNameComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.objectNameLabel = QLabel(self.centralwidget)
        self.objectNameLabel.setObjectName(u"objectNameLabel")
        self.objectNameLabel.setGeometry(QRect(490, 290, 94, 20))
        self.objectNameLabel.setFont(font1)
        self.objectTypeComboBox = QComboBox(self.centralwidget)
        self.objectTypeComboBox.setObjectName(u"objectTypeComboBox")
        self.objectTypeComboBox.setGeometry(QRect(310, 310, 171, 26))
        self.objectTypeComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.previewTableWidget = QTableWidget(self.centralwidget)
        self.previewTableWidget.setObjectName(u"previewTableWidget")
        self.previewTableWidget.setGeometry(QRect(20, 370, 911, 261))
        self.previewTableWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.previewLabel = QLabel(self.centralwidget)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setGeometry(QRect(20, 350, 69, 20))
        self.previewLabel.setFont(font1)
        self.exportPushButton = QPushButton(self.centralwidget)
        self.exportPushButton.setObjectName(u"exportPushButton")
        self.exportPushButton.setGeometry(QRect(810, 310, 121, 26))
        self.exportPushButton.setFont(font1)
        self.exportPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exportPushButton.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.qualifierGroupBox = QGroupBox(self.centralwidget)
        self.qualifierGroupBox.setObjectName(u"qualifierGroupBox")
        self.qualifierGroupBox.setGeometry(QRect(740, 20, 191, 221))
        self.qualifierGroupBox.setFont(font)
        self.withoutRadioButton = QRadioButton(self.qualifierGroupBox)
        self.withoutRadioButton.setObjectName(u"withoutRadioButton")
        self.withoutRadioButton.setGeometry(QRect(10, 30, 88, 26))
        self.withoutRadioButton.setFont(font)
        self.withoutRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.withoutRadioButton.setCheckable(True)
        self.withoutRadioButton.setChecked(False)
        self.doubleQuotationmarkRadioButton = QRadioButton(self.qualifierGroupBox)
        self.doubleQuotationmarkRadioButton.setObjectName(u"doubleQuotationmarkRadioButton")
        self.doubleQuotationmarkRadioButton.setGeometry(QRect(10, 80, 136, 26))
        self.doubleQuotationmarkRadioButton.setFont(font)
        self.doubleQuotationmarkRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.quotationmarkRadioButton = QRadioButton(self.qualifierGroupBox)
        self.quotationmarkRadioButton.setObjectName(u"quotationmarkRadioButton")
        self.quotationmarkRadioButton.setGeometry(QRect(10, 130, 167, 26))
        self.quotationmarkRadioButton.setFont(font)
        self.quotationmarkRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.otherQualifierRadioButton = QRadioButton(self.qualifierGroupBox)
        self.otherQualifierRadioButton.setObjectName(u"otherQualifierRadioButton")
        self.otherQualifierRadioButton.setGeometry(QRect(10, 180, 55, 26))
        self.otherQualifierRadioButton.setFont(font)
        self.otherQualifierRadioButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.qualifierLineEdit = QLineEdit(self.qualifierGroupBox)
        self.qualifierLineEdit.setObjectName(u"qualifierLineEdit")
        self.qualifierLineEdit.setGeometry(QRect(70, 180, 31, 26))
        self.qualifierLineEdit.setFont(font)
        self.settngsFrame = QFrame(self.centralwidget)
        self.settngsFrame.setObjectName(u"settngsFrame")
        self.settngsFrame.setGeometry(QRect(10, 30, 471, 241))
        self.settngsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settngsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.settngsFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.dbSettingsLabel = QLabel(self.settngsFrame)
        self.dbSettingsLabel.setObjectName(u"dbSettingsLabel")
        self.dbSettingsLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.dbSettingsLabel)

        self.serverLabel = QLabel(self.settngsFrame)
        self.serverLabel.setObjectName(u"serverLabel")
        self.serverLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.serverLabel)

        self.serverLineEdit = QLineEdit(self.settngsFrame)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        self.serverLineEdit.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.serverLineEdit)

        self.portLabel = QLabel(self.settngsFrame)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.portLabel)

        self.portLineEdit = QLineEdit(self.settngsFrame)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.portLineEdit)

        self.databaseLabel = QLabel(self.settngsFrame)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.databaseLabel)

        self.databaseLineEdit = QLineEdit(self.settngsFrame)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.databaseLineEdit)

        self.userNameLabel = QLabel(self.settngsFrame)
        self.userNameLabel.setObjectName(u"userNameLabel")
        self.userNameLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.userNameLabel)

        self.userNameLineEdit = QLineEdit(self.settngsFrame)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")
        self.userNameLineEdit.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.userNameLineEdit)

        self.passwordLabel = QLabel(self.settngsFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.settngsFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.testConnectionPushButton = QPushButton(self.settngsFrame)
        self.testConnectionPushButton.setObjectName(u"testConnectionPushButton")
        self.testConnectionPushButton.setFont(font1)
        self.testConnectionPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.testConnectionPushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.testConnectionPushButton)

        self.databaseComboBox = QComboBox(self.centralwidget)
        self.databaseComboBox.setObjectName(u"databaseComboBox")
        self.databaseComboBox.setGeometry(QRect(20, 310, 281, 24))
        self.chooseDatabaseLabel = QLabel(self.centralwidget)
        self.chooseDatabaseLabel.setObjectName(u"chooseDatabaseLabel")
        self.chooseDatabaseLabel.setGeometry(QRect(20, 290, 107, 20))
        self.chooseDatabaseLabel.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 952, 33))
        self.menuOhje = QMenu(self.menubar)
        self.menuOhje.setObjectName(u"menuOhje")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.serverLineEdit, self.portLineEdit)
        QWidget.setTabOrder(self.portLineEdit, self.databaseLineEdit)
        QWidget.setTabOrder(self.databaseLineEdit, self.userNameLineEdit)
        QWidget.setTabOrder(self.userNameLineEdit, self.passwordLineEdit)
        QWidget.setTabOrder(self.passwordLineEdit, self.testConnectionPushButton)
        QWidget.setTabOrder(self.testConnectionPushButton, self.semicolonRadioButton)
        QWidget.setTabOrder(self.semicolonRadioButton, self.commaRadioButton)
        QWidget.setTabOrder(self.commaRadioButton, self.tabRadioButton)
        QWidget.setTabOrder(self.tabRadioButton, self.otherSeparatorRadioButton)
        QWidget.setTabOrder(self.otherSeparatorRadioButton, self.separatorLineEdit)
        QWidget.setTabOrder(self.separatorLineEdit, self.withoutRadioButton)
        QWidget.setTabOrder(self.withoutRadioButton, self.doubleQuotationmarkRadioButton)
        QWidget.setTabOrder(self.doubleQuotationmarkRadioButton, self.quotationmarkRadioButton)
        QWidget.setTabOrder(self.quotationmarkRadioButton, self.otherQualifierRadioButton)
        QWidget.setTabOrder(self.otherQualifierRadioButton, self.qualifierLineEdit)
        QWidget.setTabOrder(self.qualifierLineEdit, self.objectTypeComboBox)
        QWidget.setTabOrder(self.objectTypeComboBox, self.objectNameComboBox)
        QWidget.setTabOrder(self.objectNameComboBox, self.previewTableWidget)
        QWidget.setTabOrder(self.previewTableWidget, self.exportPushButton)

        self.menubar.addAction(self.menuOhje.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.separatorGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sarake-erotin", None))
        self.semicolonRadioButton.setText(QCoreApplication.translate("MainWindow", u"puolipiste (;)", None))
        self.commaRadioButton.setText(QCoreApplication.translate("MainWindow", u"pilkku (,)", None))
        self.tabRadioButton.setText(QCoreApplication.translate("MainWindow", u"Sarkain", None))
        self.otherSeparatorRadioButton.setText(QCoreApplication.translate("MainWindow", u"Muu", None))
        self.objectTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin tyyppi", None))
        self.objectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin nimi", None))
        self.previewLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.exportPushButton.setText(QCoreApplication.translate("MainWindow", u"Vie tiedostoon", None))
        self.qualifierGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tekstin tunniste", None))
        self.withoutRadioButton.setText(QCoreApplication.translate("MainWindow", u"Ei mit\u00e4\u00e4n", None))
        self.doubleQuotationmarkRadioButton.setText(QCoreApplication.translate("MainWindow", u"lainausmerkki (\")", None))
        self.quotationmarkRadioButton.setText(QCoreApplication.translate("MainWindow", u"puolilainausmerkki (')", None))
        self.otherQualifierRadioButton.setText(QCoreApplication.translate("MainWindow", u"Muu", None))
        self.dbSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokantayhteyden asetukset", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.serverLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Palvelimen nimi tai IP-osoite", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TCP-portin numero, oletus 5432", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.databaseLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tietokannan nimi, hallintatietokanta postgres", None))
        self.userNameLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.userNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus, oletusp\u00e4\u00e4k\u00e4ytt\u00e4j\u00e4 postgres", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4n salasana", None))
        self.testConnectionPushButton.setText(QCoreApplication.translate("MainWindow", u"Testaa yhteys", None))
        self.chooseDatabaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.menuOhje.setTitle(QCoreApplication.translate("MainWindow", u"Ohje", None))
    # retranslateUi

