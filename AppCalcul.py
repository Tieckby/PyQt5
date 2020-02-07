#coding:utf-8

#Quelques modules nécessaires pour la création de l'application 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QMenuBar, QAction, QMessageBox, QDialog, QComboBox, QLabel, QLineEdit, QVBoxLayout)
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

import sys #Importation des ressources système

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #Queques infos de la fenêtre (Titre, Position, Taille)
        self.title = "Application de calcul"
        self.top = 100
        self.left = 100
        self.width = 700
        self.height = 500
        self.icon = "Cal.png"

        self.InitWindow() #Appel de la méthode InitWindow()

    #La methode qui permet de créer la fenêtre
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon)) #L'icône de la fenêtre
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.appMenu()
        self.comboBox()
        self.show() #Affiche la fenêtre
    
    def comboBox(self):
        vbox = QVBoxLayout()

        self.combo = QComboBox(self)

        for i in range(1, 10):
            self.combo.addItem(f"{i}")
        self.combo.move(50, 50)
        self.combo.currentTextChanged.connect(self.comboSelect)

    def comboSelect(self):
        try:
            number = int(self.combo.currentText())
            if number in range(1, 10):
                for i in range(1,  11):
                    res = number * i
                    print(f"{number} * {i} = {res}")
        except:
            pass
    
    def onPressedEntry(self):
        self.label.setText(self.lineedit.text())
    
    # def lineEdit(self):
    #     widget = QWidget()
    #     self.setCentralWidget(widget)

    #     #Ajout du texte à la fenêtre
    #     layout = QVBoxLayout()
    #     # widget.setLayout(layout)

    #     self.label = QLabel(self)
    #     # label.setStyleSheet('color:green') #Coleur du texte

    #     layout.addWidget(self.label)

    #     #Ajout d'un champ QLineEdit
    #     lineedit = QLineEdit(self)
    #     lineedit.setFont(QtGui.QFont("Sanserif", 10)) #Le style et la taille de la saisie
    #     resultInput = lineedit.returnPressed.connect(self.onPressedEntry) #On capture la saisie et on l'affiche
    #     layout.addWidget(lineedit)

    #     label1 = QLabel(f"Le resultat est : {resultInput}")
    #     label1.setFont(QtGui.QFont("Sanserif", 20))
    #     layout.addWidget(label1)
    
    #Création du menu
    def appMenu(self):
        mainMenu = self.menuBar()

        #Menu
        calculOperationMenu = mainMenu.addMenu("Opération de calcul")
        operatorTable = mainMenu.addMenu("Table des opérations")
        helpApp = mainMenu.addMenu("Aide")
        exitApp = mainMenu.addMenu("Quitter")

        #Action sur les différentes Menu
        calculOperationMenuAction = QAction(QIcon("Calc.png"), 'Calcul simple', self)
        calculOperationMenuAction.setShortcut("CTRL+E")
        # calculOperationMenuAction.triggered.connect(self.lineEdit)
        calculOperationMenu.addAction(calculOperationMenuAction)

        add = QAction(QIcon("Calc.png"), "Addition", self)
        add.triggered.connect(self.comboBox)
        operatorTable.addAction(add)
        subs = QAction(QIcon("Calc.png"), "Soustraction", self)
        subs.triggered.connect(self.comboBox)
        operatorTable.addAction(subs)
        mult = QAction(QIcon("Calc.png"), "Mutiplication", self)
        mult.triggered.connect(self.comboBox)
        operatorTable.addAction(mult)
        divid = QAction(QIcon("Calc.png"), "Division", self)
        divid.triggered.connect(self.comboBox)
        operatorTable.addAction(divid)

        helpAppAction = QAction(QIcon("help.png"), 'A propos', self)
        helpAppAction.setShortcut("CTRL+H")
        helpAppAction.triggered.connect(self.helpfonction)
        helpApp.addAction(helpAppAction)

        exitAppAction = QAction(QIcon("exit.png"), 'quitter', self)
        exitAppAction.setShortcut("CTRL+X")
        exitAppAction.triggered.connect(self.exitFonction)
        exitApp.addAction(exitAppAction)

    def helpfonction(self):
        message = QMessageBox.about(self, "Aide à propos de l'application", "Bienvenu dans dans cette application de calcul\nVous pouvez voir la table des opérateurs ou faire des calculs de nombres...\n\tMerci... : !)")
    
    def exitFonction(self):
        self.close()

if __name__=="__main__":
    #Les instances Application et de Window
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec()) #Point de sorti du programme