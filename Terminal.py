#coding:utf-8
"""___Mini terminal__"""
import time
command = ""
user_name = "Default"
terminal_launched = True

while terminal_launched:
    command = input(f"\n#{user_name}~ ")
    if command == "run":
        for i in range(0, 4):
            print("\nT")
            time.sleep(1)
    elif command == "name":
        user_name = input("\n\tSaisir un nouveau nom du terminal : ")
    elif command == "kill":
        ip = input("\n\tDonner l'ip de la victime : ")
        print(f"\n\t\tVous venez de détruire la machine {ip} du réseau courant !")
    elif command == "help":
        print("\n> Commandes disponibles :\n\t- run (affiche 4 fois la lettre 'T' avec une pause entre chaque seconde de 1s)\n\t- kill (Détruit une machine en lui spécifiant une ip)\n\t- help (affiche la liste des commandes)\n\t- quit (quitter le terminal)")
    elif command == "quit":
        terminal_launched = False
    else:
        print("\nError : commande non reconnu...")