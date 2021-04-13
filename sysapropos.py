# HERMAN Adrien
# 8 Avril 2021

# Modules de Python
from PyQt5 import QtWidgets

# Modules du logiciel
from apropos_ui import Ui_apropos


class AProposWindow(QtWidgets.QMainWindow, Ui_apropos):
    def __init__(self, parent=None):
        """
        :rtype: object
        """
        super(AProposWindow, self).__init__(parent)
        self.setupUi(self)