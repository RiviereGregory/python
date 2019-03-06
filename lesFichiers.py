# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:06:35 2019

@author: Greg13
"""

# Ouvrir un fichier
monFichier = open("fichier.txt","r")
monFichier
type(monFichier)

# fermer le fichier
monFichier.close()

# lire le fichier en entier
monFichier = open("fichier.txt","r")
contenu = monFichier.read()
print(contenu)
monFichier.close()


# Ecrire dans un fichier
monFichier = open("fichier.txt","w")
monFichier.write("Premier test d'écriture dans un fichier")
monFichier.close()

# protection avec with
with open("fichier.txt","r") as monFichier :
    texte = monFichier.read()

print(texte)

monFichier.closed    

# enregistrer des objets
import pickle
fruits = {"melons":3,"pommes":51,"poires":36}
with open('donnees','wb') as fichier :
    monPikler = pickle.Pickler(fichier)  
    monPikler.dump(fruits)
    
# Récupérer l'objet
with open('donnees','rb') as fichier :
    monPikler = pickle.Unpickler(fichier)  
    fruitsRecuperer = monPikler.load()
    
fruitsRecuperer



fruits = {"melons":7,"pommes":32,"poires":21}
scores = {"Joueur1":3,"Joueur2":5,"Joueur3":3,"Joueur4":15}
with open('donnees','wb') as fichier :
    monPikler = pickle.Pickler(fichier)  
    monPikler.dump(fruits)
    monPikler.dump(scores)
    
# Récupérer l'objet
with open('donnees','rb') as fichier :
    monPikler = pickle.Unpickler(fichier)  
    fruitsRecuperer = monPikler.load()
    scoresRecuperer = monPikler.load()
    
print(fruitsRecuperer)
print(scoresRecuperer)




