# HERMAN Adrien
# 8 Avril 2021

# Modules de Python
from PyQt5 import QtGui, QtWidgets

# Modules du logiciel
from modifier_ui import Ui_ModifierListe
import SelectFile


class ModifierWindow(QtWidgets.QMainWindow, Ui_ModifierListe):
    def __init__(self, parent=None):
        """
        :rtype: object
        """
        super(ModifierWindow, self).__init__(parent)
        self.setupUi(self)

        # ComboBox
        self.listemot.currentIndexChanged.connect(self.UpdateMot)

        # Boutons
        self.openvoca.clicked.connect(self.OuvrirListe)
        self.save.clicked.connect(self.SaveFile)
        self.modifmot.clicked.connect(self.ModifMot)
        self.supprmot.clicked.connect(self.SupprMot)
        self.addmot.clicked.connect(self.AddMot)

        # Raccourcis Clavier
        # Raccourcis Clavier
        self.shortcut_enter = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self)
        self.shortcut_enter.activated.connect(self.AddMot)
        self.shortcut_save = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.shortcut_save.activated.connect(lambda: self.SaveFile(False))

        self.OuvrirListe()

    def OuvrirListe(self):
        """
        Ouvrir une liste de vocabulaire.
        :return: None
        """
        self.chercher_fichier = SelectFile.SelectFile()
        self.filepath = self.chercher_fichier.getFileName()

        if self.ParseData():
            self.cheminfichier.setText(self.filepath)
            self.liste = [self.mot[i] + " / " + self.trad[i] for i in range(len(self.mot))]

            self.UpdateCombobox()

            self.UpdateMot()

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

    def ParseData(self):
        """
        Aller chercher tous les mots et leurs signification dans le fichier.
        Retourne True si le fichier peut être lu, et false sinon.
        :return: Boolean
        """
        if self.filepath != None:
            file = open(self.filepath, 'r')
            data = file.read().split("\n")
            data.remove("")
            file.close()

            self.mot = [d.split("|")[0] for d in data]
            self.trad = [d.split("|")[1] for d in data]

            return True

        return False

    def SaveFile(self, destroy = True):
        """
        Sauvegarder le fichier de vocabulaire modifié.
        :return: None
        """
        if self.filepath != None:
            file = open(self.filepath, "w+")

            for mot, trad in zip(self.mot, self.trad):
                    file.write(mot + "|" + trad + "\n")

            file.close()

            if destroy: self.destroy()
        else:
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