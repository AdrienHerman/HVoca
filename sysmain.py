# HERMAN Adrien
# 8 Avril 2021
# 1146 lignes

# Modules de Python
from random import randint
from PyQt5 import QtGui, QtWidgets

# Modules du logiciel
import SelectFile
from app_ui import Ui_MainWindow
from sysapropos import AProposWindow
from sysfauxui import FauxWindow
from sysmodifier import ModifierWindow
from sysnouveau import NouveauWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """
        :rtype: object
        """
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("icon/icon.png"))

        # Vairiables d'environnement
        self.mot = []
        self.trad = []
        self.modeinverse = False

        # Menubar
        #       Fichier
        self.ui.actionNouvelle_liste_de_vocabulaire.triggered.connect(self.NouvelleListe)
        self.ui.actionOuvrir_une_liste_de_vocabulaire.triggered.connect(self.OuvrirListe)
        self.ui.actionModifier_une_liste_de_vocabulaire.triggered.connect(self.ModifierListe)
        self.ui.actionQuitter.triggered.connect(QtWidgets.QApplication.quit)
        #       Aide
        self.ui.action_propos.triggered.connect(self.APropos)

        # Boutons
        self.ui.prop1.clicked.connect(lambda: self.Reponse(1))
        self.ui.prop2.clicked.connect(lambda: self.Reponse(2))
        self.ui.prop3.clicked.connect(lambda: self.Reponse(3))
        self.ui.jcp.clicked.connect(lambda: self.Reponse(0))

        # CheckBox
        self.ui.modeinverse.clicked.connect(self.Inverse)

        # Ouvrir un fichier de vocabulaire
        self.chercher_fichier = SelectFile.SelectFile()
        self.filepath = self.chercher_fichier.getFileName()
        self.show()
        self.activateWindow()

        self.Jeu()

    def Inverse(self):
        """
        Activer / Désactiver le mode inversé.
        :return: None
        """
        if self.ui.modeinverse.isChecked():
            self.modeinverse = True
        else:
            self.modeinverse = False

        self.Jeu()

    def NouvelleListe(self):
        """
        Ouverture de la fenêtre Nouvelle liste.
        :return: None
        """
        window = NouveauWindow(self)
        window.show()

    def OuvrirListe(self):
        """
        Ouvrir une liste de vocabulaire.
        :return: None
        """
        self.chercher_fichier = SelectFile.SelectFile()
        self.filepath = self.chercher_fichier.getFileName()
        self.activateWindow()
        if self.filepath is not None: self.Jeu()

    def ModifierListe(self):
        """
        Ouverture de la fenêtre Modifier la liste.
        :return: None
        """
        window = ModifierWindow(self)
        window.show()

    def APropos(self):
        """
        Ouverture de la fenêtre À Propos.
        :return: None
        """
        window = AProposWindow(self)
        window.show()

    def ViderTout(self):
        """
        Remise de la fenêtre à son état initial.
        :return: None
        """
        self.ui.motvoca.setText("Mot de vocabulaire")
        self.ui.prop1.setText("Proposition 1")
        self.ui.prop2.setText("Proposition 2")
        self.ui.prop3.setText("Proposition 3")
        self.ui.score.setText("XX / YY")
        self.ui.modeinverse.setCheckState(False)
        self.modeinverse = False
        self.mot = []
        self.trad = []
        self.mot_q = []
        self.trad_q = []
        self.index = []
        self.index_q = -1
        self.score = 0
        self.nb_mots = 0
        self.filepath = None

    def Reponse(self, bouton):
        """
        Déclenchement de la réponse de l'utilisateur et vérification de la réponse.
        :param bouton: Numéro du bouton appuyé
        :return: None
        """
        correct = False

        if self.modeinverse:
            if len(self.mot_q) > 2:
                if bouton == 0:
                    window = FauxWindow(self)
                    window.show()
                elif bouton == 1 and self.ui.prop1.text() == self.mot_q[self.index_q]:
                    correct = True
                elif bouton == 2 and self.ui.prop2.text() == self.mot_q[self.index_q]:
                    correct = True
                elif bouton == 3 and self.ui.prop3.text() == self.mot_q[self.index_q]:
                    correct = True
            else:
                if bouton == 0:
                    window = FauxWindow(self)
                    window.show()
                elif bouton == 1 and self.ui.prop1.text() == self.mot[self.index[self.index_q]]:
                    correct = True
                elif bouton == 2 and self.ui.prop2.text() == self.mot[self.index[self.index_q]]:
                    correct = True
                elif bouton == 3 and self.ui.prop3.text() == self.mot[self.index[self.index_q]]:
                    correct = True
        else:
            if len(self.mot_q) > 2:
                if bouton == 0:
                    window = FauxWindow(self)
                    window.show()
                elif bouton == 1 and self.ui.prop1.text() == self.trad_q[self.index_q]:
                    correct = True
                elif bouton == 2 and self.ui.prop2.text() == self.trad_q[self.index_q]:
                    correct = True
                elif bouton == 3 and self.ui.prop3.text() == self.trad_q[self.index_q]:
                    correct = True
            else:
                if bouton == 0:
                    window = FauxWindow(self)
                    window.show()
                elif bouton == 1 and self.ui.prop1.text() == self.trad[self.index[self.index_q]]:
                    correct = True
                elif bouton == 2 and self.ui.prop2.text() == self.trad[self.index[self.index_q]]:
                    correct = True
                elif bouton == 3 and self.ui.prop3.text() == self.trad[self.index[self.index_q]]:
                    correct = True

        if correct and len(self.mot_q) > 2:
            self.mot_connus += 1
            del self.mot_q[self.index_q]
            del self.trad_q[self.index_q]

            self.UpdateScore()
        elif correct and len(self.mot_q) <= 2:
            self.mot_connus += 1
            del self.mot_q[0]
            del self.trad_q[0]

            self.UpdateScore()
        else:
            window = FauxWindow(self)
            window.show()

        if self.TirerMots():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Bravo!")
            msg.setText("Bravo! Tu connais tous les mots de vocabulaire de la liste!")
            msg.exec()

            self.ViderTout()

    def UpdateMot(self):
        """
        Mettre à jour les traductions suggérés dans les boutons et le mot dans le label.
        :return: None
        """
        if self.modeinverse:
            if len(self.mot_q) > 2:
                self.ui.prop1.setText(self.mot_q[self.index[0]])
                self.ui.prop2.setText(self.mot_q[self.index[1]])
                self.ui.prop3.setText(self.mot_q[self.index[2]])
                self.ui.motvoca.setText(self.trad_q[self.index_q])
            else:
                self.ui.prop1.setText(self.mot[self.index[0]])
                self.ui.prop2.setText(self.mot[self.index[1]])
                self.ui.prop3.setText(self.mot[self.index[2]])
                self.ui.motvoca.setText(self.trad[self.index[self.index_q]])
        else:
            if len(self.mot_q) > 2:
                self.ui.prop1.setText(self.trad_q[self.index[0]])
                self.ui.prop2.setText(self.trad_q[self.index[1]])
                self.ui.prop3.setText(self.trad_q[self.index[2]])
                self.ui.motvoca.setText(self.mot_q[self.index_q])
            else:
                self.ui.prop1.setText(self.trad[self.index[0]])
                self.ui.prop2.setText(self.trad[self.index[1]])
                self.ui.prop3.setText(self.trad[self.index[2]])
                self.ui.motvoca.setText(self.mot[self.index[self.index_q]])

    def UpdateScore(self):
        """
        Mettre à jour le score dans la fenêtre.
        :return: None
        """
        self.ui.score.setText("{0} / {1}".format(self.mot_connus, self.nb_mots))

    def TirerMots(self):
        """
        Tirer aléatoirement les 3 traductions suggérées.
        :return: Boolean
        """

        # Choix aléatoire des mots
        if len(self.mot_q) > 2:
            self.index = [randint(0, len(self.mot_q) - 1) for _ in range(3)]

            while self.index[0] == self.index[1] or self.index[0] == self.index[2] or self.index[1] == self.index[2]:
                self.index = [randint(0, len(self.mot_q) - 1) for _ in range(3)]

            self.index_q = self.index[randint(0, 2)]
        elif len(self.mot_q) == 2:
            self.index = [randint(0, 1) for _ in range(2)]

            while self.index[0] == self.index[1]:
                self.index = [randint(0, 1) for _ in range(2)]

            self.index.append(randint(0, len(self.mot) - 1))

            self.index_q = randint(0, 1)
            self.index[0] = self.mot.index(self.mot_q[self.index[0]])
            self.index[1] = self.mot.index(self.mot_q[self.index[1]])
        elif len(self.mot_q) == 1:
            self.index = [randint(0, self.nb_mots - 1) for _ in range(3)]

            while self.index[0] == self.index[1] or self.index[0] == self.index[2] or self.index[1] == self.index[2]:
                self.index = [randint(0, self.nb_mots - 1) for _ in range(3)]

            self.index_q = randint(0, 2)

            self.index[self.index_q] = self.mot.index(self.mot_q[0])
        else:
            return True

        self.UpdateMot()

    def Jeu(self):
        """
        Début du jeu.
        :return: None
        """
        # Récupérer les mots
        if self.ParseData():
            # Variables du jeu
            self.mot_q = [mot for mot in self.mot]
            self.trad_q = [trad for trad in self.trad]
            self.mot_connus = 0
            self.nb_mots = len(self.mot)

            # Score en cours
            self.UpdateScore()

            self.TirerMots()

    def ParseData(self):
        """
        Aller chercher tous les mots et leurs signification dans le fichier.
        Retourne True si le fichier peut être lu, et false sinon.
        :return: Boolean
        """
        try:
            file = open(self.filepath, 'r')
            data = file.read().split("\n")
            data.remove("")
            file.close()

            self.mot = [d.split("|")[0] for d in data]
            self.trad = [d.split("|")[1] for d in data]

            if len(self.mot) > 2:   return True

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("ERREUR")
            msg.setText("Impossible de charger la liste de vocabulaire, elle ne contient pas assez de mots!")
            msg.exec()

            return False
        except:
            return False
