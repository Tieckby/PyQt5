from tkinter import *
import math
from tkinter.font import Font as f

def evaluer(event):
    chaine.configure(text="Resultat : "+str(eval(entree.get())))

fen = Tk()
fen.title("Calculatrice")
fen.geometry("500x500")
entree = Entry(fen, width=30)
entree.bind("<Return>", evaluer)
entree.config(font = f(size=30))
chaine = Label(fen, fg='red')
chaine.config(font = f(size=30))
entree.pack()
chaine.pack()
fen.mainloop()