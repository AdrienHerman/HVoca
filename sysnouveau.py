# HERMAN Adrien
# 8 Avril 2021

# Modules de Python
from PyQt5 import QtGui, QtWidgets

# Modules du logiciel
from nouveau_ui import Ui_NouvelleListe
import SaveFile


class NouveauWindow(QtWidgets.QMainWindow, Ui_NouvelleListe):
    def __init__(self, parent=None):
        """
        :rtype: object
        """
        super(NouveauWindow, self).__init__(parent)
        self.setupUi(self)

        # Variables d'environnement
        self.mot = []
        self.trad = []
        self.liste = []

        # ComboBox
        self.listemot.currentIndexChanged.connect(self.UpdateMot)

        # Boutons
        self.save.clicked.connect(self.SaveList)
        self.modifmot.clicked.connect(self.ModifMot)
        self.supprmot.clicked.connect(self.SupprMot)
        self.addmot.clicked.connect(self.AddMot)

        # Raccourcis Clavier
        self.shortcut_enter = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self)
        self.shortcut_enter.activated.connect(self.AddMot)
        self.shortcut_save = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.shortcut_save.activated.connect(lambda : self.SaveList(False))

    def UpdateMot(self):
        """
        Mettre à jour le mot dans les lignes d'édition.
        :return: None
        """
        if len(self.liste) > 0:
            self.motedit.setText(self.mot[self.listemot.currentIndex()])
            self.tradedit.setText(self.trad[self.listemot.currentIndex()])
        else:
            self.motedit.setText("")
            self.tradedit.setText("")

    def SaveList(self, destroy=True):
        """
        Sauvegarder le fichier de vocabulaire modifié.
        :return: None
        """

        if len(self.mot) > 2:
            self.sauvegarder = SaveFile.SaveFile()
            self.filepath = self.sauvegarder.getFileName()
            self.activateWindow()
            continuer = True
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERREUR")
            msg.setText("Impossible d'enregistrer le fichier: Il n'y a pas assez de mots dans la liste!")
            msg.exec()
            continuer = False
            self.filepath = None

        if self.filepath != None and continuer:
            self.filepath = self.filepath.split(".")
            self.filepath = self.filepath[0]
            file = open(self.filepath + ".vocab", "w+")

            for mot, trad in zip(self.mot, self.trad):
                file.write(mot + "|" + trad + "\n")

            file.close()

            if destroy: self.destroy()
        elif self.filepath == None and continuer:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERREUR")
            msg.setText("Impossible d'enregistrer le fichier!")
            msg.exec()

    def ModifMot(self):
        """
        Modifier le fichier dans la liste.
        :return: None
        """
        self.mot[self.listemot.currentIndex()] = self.motedit.text()
        self.trad[self.listemot.currentIndex()] = self.tradedit.text()
        self.liste[self.listemot.currentIndex()] = self.motedit.text() + " / " + self.tradedit.text()
        self.UpdateCombobox()

    def SupprMot(self):
        """
        Supprimer un mot de la liste.
        :return: None
        """
        if len(self.liste) > 0:
            del self.liste[self.listemot.currentIndex()]
            del self.mot[self.listemot.currentIndex()]
            del self.trad[self.listemot.currentIndex()]
            self.UpdateCombobox()

    def UpdateCombobox(self):
        """
        Effacer puis remplir la liste de mots.
        :return: None
        """
        self.listemot.clear()
        self.listemot.addItems(self.liste)

    def AddMot(self):
        """
        Ajouter un mot à la liste de mots.
        :return: None
        """
        mot = self.motedit.text()
        trad = self.tradedit.text()
        index_mot = -1
        index_trad = -2

        try:    index_mot = self.mot.index(mot)
        except: pass

        try:    index_trad = self.trad.index(trad)
        except: pass

        if index_trad != index_mot and mot != "" and trad != "":
            self.mot.append(mot)
            self.trad.append(trad)
            self.liste.append(mot + " / " + trad)
            self.UpdateCombobox()

        self.motedit.setText("")
        self.tradedit.setText("")
        self.motedit.setFocus()