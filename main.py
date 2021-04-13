# HERMAN Adrien
# 8 Avril 2021

# Modules de Python
import sys
from PyQt5 import QtCore, QtWidgets

# Module du logiciel
from sysmain import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    window.show()
    sys.exit(app.exec_())