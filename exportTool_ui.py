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
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 770)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dbSettingsFrame = QFrame(self.centralwidget)
        self.dbSettingsFrame.setObjectName(u"dbSettingsFrame")
        self.dbSettingsFrame.setGeometry(QRect(10, 0, 1041, 302))
        self.dbSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dbSettingsFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.gridLayout = QGridLayout(self.dbSettingsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.databaseLineEdit = QLineEdit(self.dbSettingsFrame)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        font = QFont()
        font.setPointSize(11)
        self.databaseLineEdit.setFont(font)

        self.gridLayout.addWidget(self.databaseLineEdit, 8, 2, 1, 1)

        self.groupBox = QGroupBox(self.dbSettingsFrame)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.radioButton_4)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit)


        self.gridLayout.addWidget(self.groupBox, 2, 4, 9, 1)

        self.portLabel = QLabel(self.dbSettingsFrame)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font)

        self.gridLayout.addWidget(self.portLabel, 7, 1, 1, 1)

        self.serverLabel = QLabel(self.dbSettingsFrame)
        self.serverLabel.setObjectName(u"serverLabel")
        self.serverLabel.setFont(font)

        self.gridLayout.addWidget(self.serverLabel, 6, 1, 1, 1)

        self.databaseLabel = QLabel(self.dbSettingsFrame)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font)

        self.gridLayout.addWidget(self.databaseLabel, 8, 1, 1, 1)

        self.dbSettingsLabel = QLabel(self.dbSettingsFrame)
        self.dbSettingsLabel.setObjectName(u"dbSettingsLabel")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.dbSettingsLabel.setFont(font1)

        self.gridLayout.addWidget(self.dbSettingsLabel, 2, 1, 1, 1)

        self.userNameLabel = QLabel(self.dbSettingsFrame)
        self.userNameLabel.setObjectName(u"userNameLabel")
        self.userNameLabel.setFont(font)

        self.gridLayout.addWidget(self.userNameLabel, 9, 1, 1, 1)

        self.passwordLabel = QLabel(self.dbSettingsFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font)

        self.gridLayout.addWidget(self.passwordLabel, 10, 1, 1, 1)

        self.testConnectionPushButton = QPushButton(self.dbSettingsFrame)
        self.testConnectionPushButton.setObjectName(u"testConnectionPushButton")
        self.testConnectionPushButton.setFont(font)
        self.testConnectionPushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.testConnectionPushButton, 11, 4, 1, 1)

        self.serverLineEdit = QLineEdit(self.dbSettingsFrame)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        self.serverLineEdit.setFont(font)

        self.gridLayout.addWidget(self.serverLineEdit, 6, 2, 1, 1)

        self.userNameLineEdit = QLineEdit(self.dbSettingsFrame)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")
        self.userNameLineEdit.setFont(font)

        self.gridLayout.addWidget(self.userNameLineEdit, 9, 2, 1, 1)

        self.portLineEdit = QLineEdit(self.dbSettingsFrame)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font)

        self.gridLayout.addWidget(self.portLineEdit, 7, 2, 1, 1)

        self.passwordLineEdit = QLineEdit(self.dbSettingsFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setFont(font)

        self.gridLayout.addWidget(self.passwordLineEdit, 10, 2, 1, 1)

        self.objectFrame = QFrame(self.centralwidget)
        self.objectFrame.setObjectName(u"objectFrame")
        self.objectFrame.setGeometry(QRect(10, 310, 1041, 401))
        self.objectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.objectFrame.setFrameShadow(QFrame.Shadow.Sunken)
        self.objectSearchFrame = QFrame(self.objectFrame)
        self.objectSearchFrame.setObjectName(u"objectSearchFrame")
        self.objectSearchFrame.setGeometry(QRect(10, 10, 1021, 91))
        self.objectSearchFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.objectSearchFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.objectSearchFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.objectTypeLabel = QLabel(self.objectSearchFrame)
        self.objectTypeLabel.setObjectName(u"objectTypeLabel")
        self.objectTypeLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.objectTypeLabel, 0, 0, 1, 1)

        self.objectNameComboBox = QComboBox(self.objectSearchFrame)
        self.objectNameComboBox.setObjectName(u"objectNameComboBox")

        self.gridLayout_2.addWidget(self.objectNameComboBox, 1, 1, 1, 1)

        self.objectTypeComboBox = QComboBox(self.objectSearchFrame)
        self.objectTypeComboBox.setObjectName(u"objectTypeComboBox")

        self.gridLayout_2.addWidget(self.objectTypeComboBox, 1, 0, 1, 1)

        self.getDataPushButton = QPushButton(self.objectSearchFrame)
        self.getDataPushButton.setObjectName(u"getDataPushButton")
        self.getDataPushButton.setFont(font)
        self.getDataPushButton.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.getDataPushButton, 1, 2, 1, 1)

        self.objectNameLabel = QLabel(self.objectSearchFrame)
        self.objectNameLabel.setObjectName(u"objectNameLabel")
        self.objectNameLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.objectNameLabel, 0, 1, 1, 1)

        self.objectPreviewFrame = QFrame(self.objectFrame)
        self.objectPreviewFrame.setObjectName(u"objectPreviewFrame")
        self.objectPreviewFrame.setGeometry(QRect(10, 100, 1021, 291))
        self.objectPreviewFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.objectPreviewFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.objectPreviewFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.previewLabel = QLabel(self.objectPreviewFrame)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setFont(font1)

        self.gridLayout_3.addWidget(self.previewLabel, 0, 0, 1, 1)

        self.previewTableWidget = QTableWidget(self.objectPreviewFrame)
        self.previewTableWidget.setObjectName(u"previewTableWidget")
        self.previewTableWidget.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.previewTableWidget, 1, 0, 2, 1)

        self.exportPushButton = QPushButton(self.objectPreviewFrame)
        self.exportPushButton.setObjectName(u"exportPushButton")
        self.exportPushButton.setFont(font)
        self.exportPushButton.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.exportPushButton, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1062, 33))
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
        QWidget.setTabOrder(self.passwordLineEdit, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.radioButton_4)
        QWidget.setTabOrder(self.radioButton_4, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.testConnectionPushButton)
        QWidget.setTabOrder(self.testConnectionPushButton, self.objectTypeComboBox)
        QWidget.setTabOrder(self.objectTypeComboBox, self.objectNameComboBox)
        QWidget.setTabOrder(self.objectNameComboBox, self.getDataPushButton)
        QWidget.setTabOrder(self.getDataPushButton, self.previewTableWidget)
        QWidget.setTabOrder(self.previewTableWidget, self.exportPushButton)

        self.menubar.addAction(self.menuOhje.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.databaseLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tietokannan nimi, hallintatietokanta postgres", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Pilkku (,)", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Puolipiste (;)", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Sarkain", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Muu", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Portti", None))
        self.serverLabel.setText(QCoreApplication.translate("MainWindow", u"Palvelin", None))
        self.databaseLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokanta", None))
        self.dbSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Tietokantayhteyden asetukset", None))
        self.userNameLabel.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Salasana", None))
        self.testConnectionPushButton.setText(QCoreApplication.translate("MainWindow", u"Testaa yhteys", None))
        self.serverLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Palvelimen nimi tai IP-osoite", None))
        self.userNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4tunnus, oletusp\u00e4\u00e4k\u00e4ytt\u00e4j\u00e4 postgres", None))
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TCP-portin numero, oletus 5432", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4n salasana", None))
        self.objectTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin tyyppi", None))
        self.getDataPushButton.setText(QCoreApplication.translate("MainWindow", u"Hae", None))
        self.objectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Objektin nimi", None))
        self.previewLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.exportPushButton.setText(QCoreApplication.translate("MainWindow", u"Vie tiedostoon", None))
        self.menuOhje.setTitle(QCoreApplication.translate("MainWindow", u"Ohje", None))
    # retranslateUi

