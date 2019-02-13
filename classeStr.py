# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:11:20 2019

@author: Greg13
"""
majuscule = "UNE CHAINE DE CRACTÈRE"
print(majuscule.lower())

minuscule = "une chaine de cractère"
print(minuscule.upper())
print(minuscule.capitalize())


espace = "   une  chaine  de cractère  "
print(espace.strip())

titre ="introduction"
print(titre.upper().center(20))

print(titre.center(20))

print(majuscule.center(40).lower())


prenom = "jean"
nom = "dupont"
age = 21
print("je m'appelle {0} {1} et j'ai {2} ans".format(prenom, nom, age))

phrase = "je m'appelle {0} {1} (administrativement Mr {3} {0})" \
" et j'ai {2} ans".format(prenom, nom, age,nom.upper())

print(phrase)

date ="21 jullet 2017"
heure = "17h30"
print("cela c'est passé le {} à {} sur Mars".format(date,heure))

adresse =""" {no_rue} , {nom_rue} {code_postal} {nom_ville} ({pays}) """\
.format(no_rue=5 , nom_rue="rue thier",code_postal="13005",\
        nom_ville="Marseille",pays="Mars")
print(adresse)

chaine ="test chaine caravtère"
print(chaine[0])
print(chaine[5])
print(chaine[-1])

print(len(chaine))
i = 0
while i < len(chaine) :
    print(chaine[i])
    i+=1

presentation ="test chaine"
print(presentation[0:3])
print(presentation[3:len(presentation)])

presentation = "nouvelle"+presentation[4:len(presentation)]
print(presentation)


