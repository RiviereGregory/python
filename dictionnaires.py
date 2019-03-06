# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:15:00 2019

@author: Greg13
"""

# créer un dictionnaire 
## 1
monDictionnaire = dict()
type(monDictionnaire)
monDictionnaire

## 2
monDictionnaire = {}
monDictionnaire["pseudo"] = "Prolixe"
monDictionnaire["mot de passe"] = "*"
monDictionnaire



monDictionnaire = {}
monDictionnaire[0] = "a"
monDictionnaire[1] = "e"
monDictionnaire[2] = "i"
monDictionnaire[3] = "o"
monDictionnaire[4] = "u"
monDictionnaire[5] = "y"
monDictionnaire


# avec tuple
echiquier = {}
echiquier['a',1] = "Tour blanche"
echiquier['b',1] = "Cavalier blanc"
echiquier['c',1] = "Fou blanc"
echiquier['d',1] = "Reine blanche"
echiquier['a',2] = "Pion blanc"
echiquier['b',2] = "Pion blanc"

echiquier

# création et affectation
placard = {"Chemise":3, "Pantalon":5, "Tee-shirt":10}
placard

# Suppression valeur
## del
del placard["Pantalon"]
placard

## pop (renvoie la valeur supprimée)
placard = {"Chemise":3, "Pantalon":5, "Tee-shirt":10}
placard.pop("Chemise")

# Avec des fonctions
print_2 = print
print_2("Afficher message")

def fete() :
    print_2("C'est la fête!!!!")

def oiseau() :
    print_2("Fais comme l'oiseau ...")

fonctions = {}
fonctions["fete"] = fete
fonctions["oiseau"] = oiseau
fonctions["oiseau"]

fonctions["oiseau"]()

# Methodes de parcours
## sur les clés
fruits = {"melons":3,"pommes":51,"poires":36}
for cle in fruits :
    print(cle)

### ou avec 
for cle in fruits.keys() :
    print(cle)

## sur les valeurs
for valeur in fruits.values() :
    print(valeur)

## sur les valeurs avec condition
if 36 in fruits.values() :
    print("un des fruits à une quantité de 36")

## Sur cle et valeurs
for cle, valeur in fruits.items() :
    print("La cle {} contient la valeur {}.".format(cle,valeur))

fruits = {"melons":3,"pommes":51,"poires":36}
quantiteARetirer = 7
for nomFruit,nbFruits in fruits.items():
    if nbFruits<quantiteARetirer :
        fruits[nomFruit] = 0
    else :
        fruits[nomFruit] = nbFruits - quantiteARetirer
        
fruits

# Fonction et paramètre dictionnaires

def fonction_inconnue(**parametres_nomme) :
    """ fonction permattant de passer un dictionnaires en entrée """
    
    print("j'ai reçue : {}.".format(parametres_nomme))

fonction_inconnue()

fonction_inconnue(p=4,j=10)

parametres ={"sep":" >> ", "end":" -\n"}
print("Voici","un","exemple","d'appel", **parametres)



