# -*- coding: utf-8 -*-

# Insertion dans liste
maListe = ['a','b','d','e']
maListe.insert(2,'c')
print(maListe)

# Concatenation
maListe1 = [1,2,5]
maListe2 = [11,9,6]

maListe1.extend(maListe2)
print(maListe1)

maListe1 = [1,2,5]
maListe2 = [11,9,6]

maListe1 += maListe2
print(maListe1)

# effacer élément
del maListe1[2]
print(maListe1)

maListe.remove('b')
print(maListe)

# Parcours de liste
maListe = ['a','b','c','d','e','f','g']
i = 0
while i < len(maListe) :
    print(maListe[i])
    i += 1
    
for elt in maListe :
    print(elt)

# enumerate
for i, elt in enumerate(maListe) :
    print("indice {} de l'élement {}".format(i,elt))


# Afficher flottant
def afficher_flottant(flottant) :
    """ fonction prenant en paramètre un flottant et renvoyant
        une chaîne de caractère reprèsentatn la troncature de ce
        nombre.La partie flottante doit avoir une longueur max
        de 3 caractères.
        Le point décimal va être rmplacé par une virgule """
    
    if type(flottant) is not float :
        raise TypeError("Le paramètre attendu doit-être un flottant")
    
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    
    return ",".join([partie_entiere,partie_flottante[:3]])


afficher_flottant(3.99999999)
afficher_flottant(1.5)
afficher_flottant(1)

# fonction multi paramètre dont le nombre est inconnu
def fonction_inconnue(*parametres) :
    """ fonction prenant n paramètres """
    
    print("j'ai reçue : {}.".format(parametres))
    
fonction_inconnue()
fonction_inconnue(33)
fonction_inconnue('a','b','c')
var = 3.5
fonction_inconnue(var,'b',33,[4],"...")

# fonction équivalente print
def afficher(*parametres, sep=' ',fin='\n') :
    parametres = list(parametres)
    for i, parametre in enumerate(parametres) :
        parametres[i]=str(parametre)
    chaine = sep.join(parametres)
    chaine+=fin
    print(chaine, end='')
    
afficher(13,"test",1,"deux",1.5)

# simple modif de liste
liste_origine =[0,1,2,3,4,5]
[nb*nb for nb in liste_origine]


liste_origine =[0,1,2,3,4,5,6,7,8,9,10]
[nb for nb in liste_origine if nb%2==0]

quantiteARetirer = 7
fruitsStockes = [15, 3, 18, 21]
[nbFruits - quantiteARetirer for nbFruits in fruitsStockes if nbFruits>quantiteARetirer]

# trie inverse d'un tuple avec sort ou sorted
inventaire = [
        ("pommes",22),
        ("melons",4),
        ("poires",18),
        ("fraises",76),
        ("prunes",51)
        ]

inventaire.sort(key=lambda tup: tup[1],reverse=True)
inventaire

inventaire2 = [
        ("pommes",22),
        ("melons",4),
        ("poires",18),
        ("fraises",76),
        ("prunes",51)
        ]
sorted_by_second = sorted(inventaire2, key=lambda tup: tup[1],reverse=True)
sorted_by_second


