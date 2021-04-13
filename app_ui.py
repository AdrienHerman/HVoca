# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/app_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 186)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.motvoca = QtWidgets.QLabel(self.centralwidget)
        self.motvoca.setObjectName("motvoca")
        self.horizontalLayout.addWidget(self.motvoca)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prop1 = QtWidgets.QPushButton(self.centralwidget)
        self.prop1.setObjectName("prop1")
        self.horizontalLayout_2.addWidget(self.prop1)
        self.prop2 = QtWidgets.QPushButton(self.centralwidget)
        self.prop2.setObjectName("prop2")
        self.horizontalLayout_2.addWidget(self.prop2)
        self.prop3 = QtWidgets.QPushButton(self.centralwidget)
        self.prop3.setObjectName("prop3")
        self.horizontalLayout_2.addWidget(self.prop3)
        self.jcp = QtWidgets.QPushButton(self.centralwidget)
        self.jcp.setObjectName("jcp")
        self.horizontalLayout_2.addWidget(self.jcp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setObjectName("score")
        self.horizontalLayout_3.addWidget(self.score)
        self.modeinverse = QtWidgets.QCheckBox(self.centralwidget)
        self.modeinverse.setStatusTip("")
        self.modeinverse.setWhatsThis("")
        self.modeinverse.setObjectName("modeinverse")
        self.horizontalLayout_3.addWidget(self.modeinverse)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 30))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFichiers = QtWidgets.QMenu(self.menubar)
        self.menuFichiers.setObjectName("menuFichiers")
        self.menu_Propos = QtWidgets.QMenu(self.menubar)
        self.menu_Propos.setObjectName("menu_Propos")
        MainWindow.setMenuBar(self.menubar)
        self.actionNouvelle_liste_de_vocabulaire = QtWidgets.QAction(MainWindow)
        self.actionNouvelle_liste_de_vocabulaire.setObjectName("actionNouvelle_liste_de_vocabulaire")
        self.actionOuvrir_une_liste_de_vocabulaire = QtWidgets.QAction(MainWindow)
        self.actionOuvrir_une_liste_de_vocabulaire.setObjectName("actionOuvrir_une_liste_de_vocabulaire")
        self.actionModifier_une_liste_de_vocabulaire = QtWidgets.QAction(MainWindow)
        self.actionModifier_une_liste_de_vocabulaire.setObjectName("actionModifier_une_liste_de_vocabulaire")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.action_propos = QtWidgets.QAction(MainWindow)
        self.action_propos.setObjectName("action_propos")
        self.menuFichiers.addAction(self.actionNouvelle_liste_de_vocabulaire)
        self.menuFichiers.addAction(self.actionModifier_une_liste_de_vocabulaire)
        self.menuFichiers.addAction(self.actionOuvrir_une_liste_de_vocabulaire)
        self.menuFichiers.addSeparator()
        self.menuFichiers.addAction(self.actionQuitter)
        self.menu_Propos.addAction(self.action_propos)
        self.menubar.addAction(self.menuFichiers.menuAction())
        self.menubar.addAction(self.menu_Propos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocabulaire"))
        self.label.setText(_translate("MainWindow", "Mot: "))
        self.motvoca.setText(_translate("MainWindow", "Mot de vocabulaire"))
        self.prop1.setText(_translate("MainWindow", "Proposition 1"))
        self.prop2.setText(_translate("MainWindow", "Proposition 2"))
        self.prop3.setText(_translate("MainWindow", "Proposition 3"))
        self.jcp.setText(_translate("MainWindow", "Je ne sais pas"))
        self.label_3.setText(_translate("MainWindow", "Nombre de mots maîtrisés: "))
        self.score.setText(_translate("MainWindow", "XX/YY"))
        self.modeinverse.setToolTip(_translate("MainWindow", "Le mode inversé propose la traduction du mot et demande à l\'utilisateur de le retrouer"))
        self.modeinverse.setText(_translate("MainWindow", "Mode inversé"))
        self.menuFichiers.setTitle(_translate("MainWindow", "Fichiers"))
        self.menu_Propos.setTitle(_translate("MainWindow", "Aide"))
        self.actionNouvelle_liste_de_vocabulaire.setText(_translate("MainWindow", "Nouvelle liste de vocabulaire"))
        self.actionNouvelle_liste_de_vocabulaire.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOuvrir_une_liste_de_vocabulaire.setText(_translate("MainWindow", "Ouvrir une liste de vocabulaire"))
        self.actionOuvrir_une_liste_de_vocabulaire.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionModifier_une_liste_de_vocabulaire.setText(_translate("MainWindow", "Modifier une liste de vocabulaire"))
        self.actionModifier_une_liste_de_vocabulaire.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))
        self.action_propos.setShortcut(_translate("MainWindow", "Ctrl+H"))