# HERMAN Adrien
# 8 Avril 2021

# Modules de Python
from PyQt5 import QtWidgets, QtGui

# Modules du logiciel
from faux_ui import Ui_MauvRep


class FauxWindow(QtWidgets.QMainWindow, Ui_MauvRep):
    def __init__(self, parent=None):
        """
        :rtype: object
        """
        super(FauxWindow, self).__init__(parent)
        self.setupUi(self)
        self.mot = parent.propmot
        self.trad = parent.proptrad[parent.index_q]

        self.motcorrige.setText(self.trad)
        self.ok.clicked.connect(self.Verif)

        # Raccourcis Clavier
        self.shortcut_enter = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self)
        self.shortcut_enter.activated.connect(self.Verif)

    def Verif(self):
        """
        Vérifier si la traduction tappée est correct et fermer la fenêtre si c'est le cas.
        :return: None
        """
        if self.mottappe.text() == self.trad:
            self.destroy()
        else:
            self.mottappe.setStyleSheet("color: rgb(255, 0, 0);")