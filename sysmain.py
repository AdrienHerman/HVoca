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
from sysliste import ListeWindow


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
        self.difficultes = []
        self.modeinverse = False
        self.partie_en_cours = False

        # Menubar
        #       Fichier
        self.ui.actionNouvelle_liste_de_vocabulaire.triggered.connect(self.NouvelleListe)
        self.ui.actionOuvrir_une_liste_de_vocabulaire.triggered.connect(self.OuvrirListe)
        self.ui.actionModifier_une_liste_de_vocabulaire.triggered.connect(self.ModifierListe)
        self.ui.actionAfficher_une_liste_de_vocabulaire.triggered.connect(self.AffListe)
        self.ui.actionConvertir_une_liste_de_vocabualire_en_pdf.triggered.connect(self.ConvListPDF)
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

    def ConvListPDF(self):
        """
        Convertir une liste de vocabulaire en fichier PDF.
        :return: None
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Patience... Cette fonctionnalit?? n'est pas encore disponible...")
        msg.exec()

    def AffListe(self):
        """
        Afficher une liste de vocabulaire.
        :return: None
        """
        window = ListeWindow(self)
        window.show()

    def Inverse(self):
        """
        Activer / D??sactiver le mode invers??.
        :return: None
        """
        if self.ui.modeinverse.isChecked():
            self.modeinverse = True
        else:
            self.modeinverse = False

        self.Jeu()

    def NouvelleListe(self):
        """
        Ouverture de la fen??tre Nouvelle liste.
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
        Ouverture de la fen??tre Modifier la liste.
        :return: None
        """
        window = ModifierWindow(self)
        window.show()

    def APropos(self):
        """
        Ouverture de la fen??tre ?? Propos.
        :return: None
        """
        window = AProposWindow(self)
        window.show()

    def ViderTout(self):
        """
        Remise de la fen??tre ?? son ??tat initial.
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
        self.difficultes = []
        self.index_q = -1
        self.propmot = ""
        self.proptrad = ["" for _ in range(3)]
        self.score = 0
        self.nb_mots = 0
        self.filepath = None
        self.partie_en_cours = False

    def Reponse(self, bouton):
        """
        D??clenchement de la r??ponse de l'utilisateur et v??rification de la r??ponse.
        :param bouton: Num??ro du bouton appuy??
        :return: None
        """
        if not self.partie_en_cours:    return

        correct = False

        if bouton == 0:
            window = FauxWindow(self)
            window.show()
        elif bouton == 1 and self.index_q == 0:
            correct = True
        elif bouton == 2 and self.index_q == 1:
            correct = True
        elif bouton == 3 and self.index_q == 2:
            correct = True

        if correct:
            self.mot_connus += 1
            del self.mot_q[self.index_mot_q]
            del self.trad_q[self.index_mot_q]

            self.UpdateScore()
        else:
            window = FauxWindow(self)
            window.show()
            self.difficultes.append([self.propmot, self.proptrad[self.index_q]])

        if self.TirerMots():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Bravo!")
            if len(self.difficultes) != 0:
                msg.setText("Bravo! Tu connais tous les mots de vocabulaire de la liste!\nVoici les mots que tu ne connais pas parfaitements:")
            else:
                msg.setText("Bravo! Tu connais tous les mots de vocabulaire de la liste!\nVoici la liste que tu viens de r??viser:")
                for i in range(self.nb_mots):   self.difficultes.append([self.mot[i], self.trad[i]])

            window = ListeWindow(self, self.difficultes)
            window.show()
            msg.exec()

            self.ViderTout()

    def UpdateMot(self):
        """
        Mettre ?? jour les traductions sugg??r??s dans les boutons et le mot dans le label.
        :return: None
        """
        self.ui.prop1.setText(self.proptrad[0])
        self.ui.prop2.setText(self.proptrad[1])
        self.ui.prop3.setText(self.proptrad[2])
        self.ui.motvoca.setText(self.propmot)

    def UpdateScore(self):
        """
        Mettre ?? jour le score dans la fen??tre.
        :return: None
        """
        self.ui.score.setText("{0} / {1}".format(self.mot_connus, self.nb_mots))

    def TirerMots(self):
        """
        Tirer al??atoirement les 3 traductions sugg??r??es.
        :return: Boolean
        """

        # Choix al??atoire des mots
        if len(self.mot_q) != 0:
            self.index = [randint(0, len(self.mot) - 1) for _ in range(3)]

            self.index_q = randint(0, 2)
            self.index_mot_q = randint(0, len(self.mot_q) - 1)
            index_mot = self.mot.index(self.mot_q[self.index_mot_q])

            while self.index[0] == self.index[1] or self.index[0] == self.index[2] or self.index[1] == self.index[2] or self.index[0] == index_mot or self.index[1] == index_mot or self.index[2] == index_mot:
                self.index = [randint(0, len(self.mot) - 1) for _ in range(3)]

            self.index[self.index_q] = self.index_mot_q

            self.propmot = self.mot_q[self.index_mot_q]
            self.proptrad = [self.trad[i] for i in self.index]
            self.proptrad[self.index_q] = self.trad_q[self.index_mot_q]

            self.UpdateMot()

            return False
        else:
            return True

    def Jeu(self):
        """
        D??but du jeu.
        :return: None
        """
        # R??cup??rer les mots
        if self.ParseData():
            # Variables du jeu
            if self.modeinverse:
                temp = [mot for mot in self.mot]
                self.mot = [trad for trad in self.trad]
                self.trad = [mot for mot in temp]

            self.mot_q = [mot for mot in self.mot]
            self.trad_q = [trad for trad in self.trad]
            self.mot_connus = 0
            self.nb_mots = len(self.mot)

            # Score en cours
            self.UpdateScore()

            self.partie_en_cours = True

            self.TirerMots()

    def ParseData(self):
        """
        Aller chercher tous les mots et leurs signification dans le fichier.
        Retourne True si le fichier peut ??tre lu, et false sinon.
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
