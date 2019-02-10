# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:25:02 2019

@author: Greg13
"""
import os

annee = input("saisie une année : " )

bissextile = False
try :
    annee = int(annee)   
    assert annee > 0
except ValueError :
    print("Erreur lors de la conversion de l'année.")
except AssertionError :
    print("""L'année saisie est inférieur ou égale à 0""")
else :
    if annee % 400 == 0 :
        bissextile = True
    elif annee % 100 == 0 :
        bissextile = False
    elif annee % 4 == 0 :
        bissextile = True
    
    if bissextile == True :
        print(str(annee) +""" est bissextile""")
    else :
        print(str(annee) +""" n'est pas bissextile""")
finally :       
    os.system("pause")
    