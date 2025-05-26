# PYSIDE6-SOVELLUS POSTGRESQL-NÄKYMIEN TIETOJEN TALLENTAMISEEN
# SCV- JA TSV-TIEDOSTOIHIN
# ============================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet

# Itsetehdyt moduulit
from customModules import dbOperations

# mainWindow_ui:n tilalle käännetyn pääikkunan tiedoston nimi ilman .py-tiedostopäätettä
from exportTool_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# --------------------------------SQL--------------------------------------
# SELECT table_name, table_type
	#   FROM information_schema.tables
	# 	    WHERE table_schema NOT IN ('information_schema', 'pg_catalog');

    # SELECT DISTINCT table_type
	#   FROM information_schema.tables
	#	    WHERE table_schema NOT IN ('information_schema', 'pg_catalog');
# --------------------------------------------------------------------------

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Tietokanta yhteys
        self.serverName = ''
        self.portNumber = ''
        self.databaseName = ''
        self.userName = ''
        self.password =  ''

        # Tietokantaobjeki
        self.dbObjectType = ''
        self.dbObjectName = ''

        # Tietokantaobjektin sarakkeiden nimet
        self.columnNamesList = []
        self.resultSet = []

        # Virheilmoitustiedot
        self.errorWindowTitle = ""
        self.errorText = ""
        self.errorDetails = ""

        # Oletustallennushakemisto
        self.defaultFolder = f'{os.path.expanduser('~')}\\Documents\\'

        # CSV-asetusten oletusarvot
        self.chosenSeparator = ';'
        self.chosenQualifier = ''
        self.ui.semicolonRadioButton.setChecked(True)
        self.ui.withoutRadioButton.setChecked(True)

        # Otetaan tietokannan valinta -yhdistelmäruutu pois käytöstä
        self.ui.databaseComboBox.setEnabled(False)
        
        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kun painetaan Testaa-painiketta, näytetään tilarivillä tulos ja päivitetään objektityyppi valinnat. Jos virhe, näytetään msgbox. Painike asettaa tietokantaparametrit ha yhteysmerkkijonon
        self.ui.testConnectionPushButton.clicked.connect(self.connectDb)

        # Kun tietokannan nimeä muokataan tarkistetaan onko se postgres jolloin aktivoidaan tietokannan yhdistelmäruutu
        self.ui.databaseLineEdit.textChanged.connect(self.activateChooseDb)

        # Kun poistutaan objektityypin valinnasta, haetaan tyypin objektilista ja päivitetään objektin nimi -valinta
        self.ui.objectTypeComboBox.currentIndexChanged.connect(self.getObjectNames)

        # TODO: Kun poistutaan / valinta on muuttunut objektilistasta näytetään Hae-painike
        self.ui.objectNameComboBox.currentIndexChanged.connect(self.updatePreview)

        # Kun hae-painiketta painetaan, päivitetään esikatselu-taulukko ja näytetään tallenna-painike  
        self.ui.exportPushButton.clicked.connect(self.saveToCSVFile)

        # Erottimen valinnan signaalit
        self.ui.commaRadioButton.clicked.connect(self.setSeparator)
        self.ui.semicolonRadioButton.clicked.connect(self.setSeparator)
        self.ui.tabRadioButton.clicked.connect(self.setSeparator)
        self.ui.otherSeparatorRadioButton.clicked.connect(self.setSeparator)
        self.ui.separatorLineEdit.textChanged.connect(self.forceOtherSeparator)

        # Teksting tunnistimien valinnan signaalit
        self.ui.withoutRadioButton.clicked.connect(self.setQualifier)
        self.ui.quotationmarkRadioButton.clicked.connect(self.setQualifier)
        self.ui.doubleQuotationmarkRadioButton.clicked.connect(self.setQualifier)
        self.ui.otherQualifierRadioButton.clicked.connect(self.setQualifier)
        self.ui.qualifierLineEdit.textChanged.connect(self.forceOtherQualifier)

    # OHJELMOIDUT SLOTIT
    # ------------------
    
    def connectDb(self):

        # Päivitetään tietokantaan liityvät ominaisuudet syötettyjen tietojen perusteella
        self.serverName = self.ui.serverLineEdit.text()
        self.portNumber = self.ui.portLineEdit.text()
        self.databaseName = self.ui.databaseLineEdit.text()
        self.userName = self.ui.userNameLineEdit.text()
        self.password = self.ui.passwordLineEdit.text()

        # Muodostetaan asetussanakirja
        settingsDictionary = {'server': self.serverName,
                      'port': self.portNumber,
                      'database': self.databaseName,
                      'userName': self.userName,
                      'password': self.password}
        
        # Jos tietokannakis on syötetty postgres, haetaan tietokantojen nimet
        if self.ui.databaseLineEdit.text() == 'postgres':
            self.ui.databaseComboBox.setEnabled(True)
        
            # Luodaan tietokantayhteysolio
            try:
                dbConnection = dbOperations.DbConnection(settingsDictionary)
                table = 'pg_catalog.pg_database'
                columns = ['datname']
                filterText = f"datistemplate = false"

                # Alustetaan objectTypes muutuja
                databaseNames = dbConnection.filterDistinctColumsFromTable(table,columns,filterText)
                dbConnection.filterColumsFromTable(table,columns,filterText)
                self.ui.statusbar.showMessage('Haettiin tietokantojen nimet')

                # Tehdään monikkolistasta merkkijonolista
                self.ui.databaseComboBox.clear()
                cleandDatabaseNameList = ['Valitse']
                for value in databaseNames:
                    databaseName = value[0]
                    cleandDatabaseNameList.append(databaseName)

                # Lisätään lista yhdistelmäruutuun
                self.ui.databaseComboBox.addItems(cleandDatabaseNameList)

            except:
                pass
        
        # Jos tietokannan nimeksi on annettu käyttjätietokanta, hateaan objektit
        else:
            # Luodaan tietokantayhteysolio
            try:
                dbConnection = dbOperations.DbConnection(settingsDictionary)
                table = 'information_schema.tables'
                columns = ['table_type']
                filterText = f"table_schema NOT IN ('information_schema', 'pg_catalog')"

                # Alustetaan objectTypes muutuja
                objectTypes = dbConnection.filterDistinctColumsFromTable(table,columns,filterText)
                dbConnection.filterColumsFromTable(table,columns,filterText)
                self.ui.statusbar.showMessage('Yhteyden muodostaminen onnistui')

                # Tehdään monikkolistasta merkkijonolista
                self.ui.objectTypeComboBox.clear()
                cleandObjectTypeList = ['Valitse']
                for value in objectTypes:
                    objectType = value[0]
                    cleandObjectTypeList.append(objectType)

                # Lisätään lista yhdistelmäruutuun
                self.ui.objectTypeComboBox.addItems(cleandObjectTypeList)

            except Exception as e:
                self.errorWindowTitle = 'Yhteys tietokantaan ei onnistunut'
                self.errorText = 'Yhteyden muodostuksessa tapahtui virhe'
                self.errorDetails = str(e)
                self.openWarning()

    # Haetaan järjestelmätaulusta tietokantaobjektien (taulujen ja näkyminen)
    def getObjectNames(self):

        # Muodostetaan asetussanakirja
        settingsDictionary = {'server': self.serverName,
                      'port': self.portNumber,
                      'database': self.databaseName,
                      'userName': self.userName,
                      'password': self.password}
        
        # Luodaan tietokantayhteysolio
        try:
            dbConnection = dbOperations.DbConnection(settingsDictionary)
            table = 'information_schema.tables'
            columns = ['table_schema','table_name']
            tableType = self.ui.objectTypeComboBox.currentText()

            filterText  = f"table_type = '{tableType}' AND table_schema NOT IN ('information_schema', 'pg_catalog')"

            objectNames = dbConnection.filterDistinctColumsFromTable(table,columns,filterText)
            self.ui.statusbar.showMessage('Haettiin tietokantaobjektien nimet')
            
            print(objectNames)

            # Tehdään monikkolistasta merkkijonolista
            self.ui.objectNameComboBox.clear() # Tyhjentää vanhat vaihtoehdot
            cleanedObjectNameList = ['Valitse']
            for value in objectNames:
                objectSchema = value[0] # Ottaa monikon ensimmäisen arvon -> skeema
                objectName = value[1] # Ottaa monikon toisen arvon -> objektin nimi
                objectFullName = f'{objectSchema}.{objectName}' # Objektin polku: skeema.nimi
                cleanedObjectNameList.append(objectFullName)
            
            # Lisätään lista yhdistelmäruutuun
            self.ui.objectNameComboBox.addItems(cleanedObjectNameList)
        
        except Exception as e:
            self.errorWindowTitle = 'Yhteys tietokantaobjektien haku ei onnistunut'
            self.errorText = 'Objektien nimien haku ei onnistunut'
            self.errorDetails = str(e)
            self.openWarning()

    def updatePreview(self):

        # Muodostetaan asetussanakirja
        settingsDictionary = {'server': self.serverName,
                      'port': self.portNumber,
                      'database': self.databaseName,
                      'userName': self.userName,
                      'password': self.password}
        
        # Luetaan valitun tietokantaobjektin skeema ja nimi
        currentObjectSelection = self.ui.objectNameComboBox.currentText()

        # Nollataan taulukko tyhjäksi
        if currentObjectSelection == 'Valitse' or currentObjectSelection == '':
            self.ui.previewTableWidget.clear()
            self.ui.previewTableWidget.setColumnCount(0)
            self.ui.previewTableWidget.setRowCount(0)
        else:
            
            # Luodaan tietokantayhteysolio
            try:
                dbConnection = dbOperations.DbConnection(settingsDictionary)
                self.resultSet = dbConnection.readAllColumnsFromTable(currentObjectSelection)
                print(self.resultSet)
        
            except:
                pass
            
            # Tyhjennetään vanhat tiedot käyttöliittymästä ennen uusien lukemista tietokannasta
            self.ui.previewTableWidget.clear()

            # Määritellään taulukkoelementin otsikot
            try:
                # Tulosjoukon rivimäärä
                numberOfRows = len(self.resultSet)
                self.ui.previewTableWidget.setRowCount(numberOfRows)

                # Tulosjoukon sarakemäärä
                columnCount = len(self.resultSet[0])
                self.ui.previewTableWidget.setColumnCount(columnCount)
                dbConnection = dbOperations.DbConnection(settingsDictionary)

                # Selvitetään sarakeotsikot j apäivitetään muuttujat
                headerRow = dbConnection.getColumnNames(currentObjectSelection)
                self.columnNamesList = headerRow
                self.ui.previewTableWidget.setHorizontalHeaderLabels(headerRow)
            
            except Exception as e:
                # TODO: Kutsu virhedialogi
                raise e
            
            # Asetetaan taulukon solujen arvot
            for row in range(numberOfRows): # Luetaan listaa riveittäin
                for column in range(len(self.resultSet[row])): # Luetaan monikkoa sarakkeittain
                    
                    # Muutetaan merkkijonoksi ja QTableWidgetItem-olioksi
                    data = QtWidgets.QTableWidgetItem(str(self.resultSet[row][column])) 
                    self.ui.previewTableWidget.setItem(row, column, data)
                    self.ui.previewTableWidget.setHorizontalHeaderLabels(headerRow)

    # Aktivoidaan muu erotin -valinta, jos erotin-kenttää on muokattu
    def forceOtherSeparator(self):
        self.ui.otherSeparatorRadioButton.setChecked(True)

    # Aktivoidaan muu tekstin tunniste -valinta, jos tunniste-kenttä on muokattu
    def forceOtherQualifier(self):
        self.ui.otherQualifierRadioButton.setChecked(True)

    # Selvitetään, miknlä erottimen käyttäjä on valinnut
    def setSeparator(self):
        if self.ui.commaRadioButton.isChecked() == True:
            self.chosenSeparator = ','
        if self.ui.semicolonRadioButton.isChecked() == True:
            self.chosenSeparator = ';'
        if self.ui.tabRadioButton.isChecked() == True:
            self.chosenSeparator = '\t'
        if self.ui.otherSeparatorRadioButton.isChecked() == True:
            self.chosenSeparator = self.ui.separatorLineEdit.text().strip()

        statusbarMessage = f'Erottimeksi on valittu {self.chosenSeparator}'
        self.ui.statusbar.showMessage(statusbarMessage, 5000)

    # Selvitetään, minkä tekstin tunnistimen käyttäjä on valinnut
    def setQualifier(self):
        if self.ui.withoutRadioButton.isChecked() == True:
            self.chosenQualifier = ''
        if self.ui.doubleQuotationmarkRadioButton.isChecked() == True:
            self.chosenQualifier = '"'
        if self.ui.quotationmarkRadioButton.isChecked() == True:
            self.chosenQualifier = "'"
        if self.ui.otherQualifierRadioButton.isChecked() == True:
            self.chosenQualifier = self.ui.qualifierLineEdit.text().strip()

        statusbarMessage = f'Tekstin tunnisteeksi on valittu {self.chosenQualifier}'
        self.ui.statusbar.showMessage(statusbarMessage, 5000)

    def createCSVdata(self, separator=';', textQualifier='"'):
        data = ''
        # Luodaan CSV-tiedoston otsikot
        headerRow = ''
        for item in self.columnNamesList:
            headerRow = headerRow + item + separator + '\n'

        # Poistetaam otikkorivin viimeinen erotinmekki
        headerRow = headerRow[:-1] # Poistetaan viimeisen sarakkeen jälkeen tuleva erotinmerkki
        headerRow = headerRow + '\\n' # Lisätään rivinvaihto

        dataRows = ''
        dataRow = ''
        for row in self.resultSet:
            for columnValue in row:
                isString = isinstance(columnValue, str)
                if isString == True:
                    columnValue = f'{textQualifier}{columnValue}{textQualifier}'
                columnValue = str(columnValue)
                dataRow = dataRow + columnValue + separator
            dataRow = dataRow [:-1]
            dataRows = dataRows + dataRow
        data = headerRow + dataRows
        return data

    # Tallennus CSV-tiedostoksi
    def saveToCSVFile(self):
        
        # Avataan tallennusdialogi oletuskanisona on käyttäjän tiedostot-kansio
        defaultFileName = f'{self.defaultFolder}{self.ui.objectNameComboBox.currentText()}'
        csvFileNameAndType = QtWidgets.QFileDialog.getSaveFileName(self, "Tallenna tiedosto",
                           defaultFileName,
                           ("CSV files (*.csv);;TSV files (*.tsv);;Text files (*.txt)"))
 
        # Otetaan monikosta polku ja tiedoston nimi
        csvFileName = csvFileNameAndType[0]

        # Avataan tiedosto kirjoittamista varten
        data = self.createCSVdata(self.chosenSeparator, self.chosenQualifier)
        with open(csvFileName, 'wt') as fileToWrite:
            fileToWrite.write(data)

        # Nollataan tiedot onnistuneen tallennuksen jälkeen
        self.resultSet = []
        self.columnNamesList = []

    # Virheilmoitusdialogi
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(self.errorWindowTitle)
        msgBox.setText(self.errorText)
        msgBox.setDetailedText(self.errorDetails)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

if __name__ == "__main__":
    # Luodaan sovellus
    app = QtWidgets.QApplication(sys.argv)

    # Asetetaan sovelluksen tyyli
    app.setStyle('Fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()