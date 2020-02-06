#coding:utf-8

#Quelques modules nécessaires pour la création de l'application 
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMenuBar, QAction, QMessageBox, QLabel, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

import sys #Importation des ressources système

class Window(QMainWindow, QDialog):
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

        #Ajout du texte et l'image à la fenêtre
        # vbox = QVBoxLayout()
        # label = QLabel("Bonjour tout le monde")
        # label.setFont(QtGui.QFont("Sanserif", 20)) #Le style et la taille
        # label.setStyleSheet('color:green') #Coleur du texte

        # vbox.addWidget(label)
        # self.setLayout(vbox)


        self.appMenu()

        self.show() #Affiche la fenêtre
    
    #Création du menu
    def appMenu(self):
        mainMenu = self.menuBar()

        #Menu
        calculOperationMenu = mainMenu.addMenu("Opération de calcul")
        operatorTable = mainMenu.addMenu("Table des opérations")
        helpApp = mainMenu.addMenu("Aide")
        exitApp = mainMenu.addMenu("Quitter")

        #Action sur les différentes Menu
        calculOperationMenuAction = QAction(QIcon("twitter_icon.png"), 'Copy',self)
        calculOperationMenuAction.setShortcut("CTRL+E")
        calculOperationMenu.addAction(calculOperationMenuAction)

        helpAppAction = QAction(QIcon("twitter_icon.png"), 'aide',self)
        helpAppAction.setShortcut("CTRL+H")
        helpAppAction.triggered.connect(self.helpfonction)
        helpApp.addAction(helpAppAction)

        exitAppAction = QAction(QIcon("twitter_icon.png"), 'quitter',self)
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