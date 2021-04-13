# HERMAN Adrien
# 8 Avril 2021

# Modules de Python
from PyQt5 import QtWidgets, QtCore

# Modules du logiciel
import SelectFile
from liste_ui import Ui_ListeWindow


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.arraydata = data

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()

        return self.arraydata[index.row()][index.column()]


class ListeWindow(QtWidgets.QMainWindow, Ui_ListeWindow):
    def __init__(self, parent=None, data=None):
        """
        :rtype: object
        """
        super(ListeWindow, self).__init__(parent)
        self.setupUi(self)

        # Menubar
        #       Fichier
        self.actionConvertir_une_liste_de_vocabualire_en_pdf.triggered.connect(self.ConvListPDF)
        self.actionOuvrir_une_liste_de_vocabulaire.triggered.connect(self.OuvrirListe)
        self.actionQuitter.triggered.connect(self.close)

        if parent.filepath != "" and data == None:
            self.filepath = parent.filepath
            self.ParseData()
            self.UpdateTable()
        elif parent.filepath == "" and data == None:
            self.OuvrirListe()
        elif data != [] and data != None:
            self.data = data
            self.filepath = "Mot de vocabulaires à revoir d'après la série précédente"
            self.UpdateTable()

    def ConvListPDF(self):
        """
        Convertir une liste de vocabulaire en fichier PDF.
        :return: None
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Patience... Cette fonctionnalité n'est pas encore disponible...")
        msg.exec()

    def UpdateTable(self):
        """
        Mise à jour du tableau.
        :return: None
        """
        self.label_2.setText(self.filepath)

        tablemodel = TableModel(self.data)
        self.tableView.setModel(tablemodel)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def OuvrirListe(self):
        """
        Ouvrir une liste de vocabulaire.
        :return: None
        """
        self.chercher_fichier = SelectFile.SelectFile()
        self.filepath = self.chercher_fichier.getFileName()
        self.ParseData()
        self.UpdateTable()

    def ParseData(self):
        """
        Aller chercher tous les mots et leurs signification dans le fichier.
        Retourne True si le fichier peut être lu, et false sinon.
        :return: None
        """
        try:
            file = open(self.filepath, 'r')
            data = file.read().split("\n")
            data.remove("")
            file.close()

            data_temp = [[d.split("|")[0], d.split("|")[1]] for d in data]

            self.data = [["Mot", "Traduction"]]
            for d in data_temp: self.data.append(d)

            if len(self.data) > 2:   return

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERREUR")
            msg.setText("Impossible de charger la liste de vocabulaire, elle ne contient pas assez de mots!")
            msg.exec()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERREUR")
            msg.setText("Impossible de charger la liste de vocabulaire!")
            msg.exec()