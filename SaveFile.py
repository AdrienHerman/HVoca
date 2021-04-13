# HERMAN Adrien
# 8 Avril 2021

# Modules de Python
import os
from sys import platform as _platform
from PyQt5 import QtWidgets

class SaveFile(object):
    def __init__(self, parent=None):
        """
        :rtype: object
        """
        if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
            self.path = os.path.expanduser("~")
        elif _platform == "win32" or _platform == "win64":
            self.path = os.path.join(os.path.expandvars("%userprofile%"),"Documents and Settings")

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(parent, "Sauvegarder la liste de vocabulaire", self.path, "Fichiers vocabulaire (*.vocab)", options = options)

    def getFileName(self):
        """
        Renvoyer le chemin du fichier sélectionné par l'utilisateur.
        :return: Chemin du fichier ou None si un problème survient.
        """
        if self.fileName:   return self.fileName
        else:               return None