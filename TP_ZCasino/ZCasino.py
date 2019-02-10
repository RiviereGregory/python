# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:44:56 2019

@author: Greg13
"""
import random
import os
import math

continuePartie = True
argent = 1000
while continuePartie :
    numeroTirage = random.randrange(50)
    
    couleurTirage = numeroTirage % 2
    
    numeroKO = True
    miseKO = True
    #print(numeroTirage)
    
    while numeroKO :
        numero = input("saisie un numéro compris entre 0 et 49 : " )    
        try :
            numero = int(numero)   
            assert numero >= 0 and numero < 50
            numeroKO = False
        except ValueError :
            print("Erreur lors de la conversion du numéro")
        except AssertionError :
            print("""Le numéro saisie doit être compris entre 0 et 49""")    
        
    while miseKO :
        print("saisie une mise supérieure à 0 et inférieure à ", str(argent)," en $ : ")
        mise = input()    
        try :
            mise = int(mise)   
            assert mise > 0 and argent >= mise
            miseKO = False
            argent = argent - mise
        except ValueError :
            print("Erreur lors de la conversion de la mise")
        except AssertionError :
            print("""La mise saisie doit être supérieure à 0 et inférieure à """, str(argent))
        
    print ("le numéro gagnant est le ",numeroTirage)
    couleurMise = numero % 2
    gain = 0
    if numeroTirage == numero:
        gain = 3*mise+mise
        print("""Vous gagnez : """, gain, """$""")
    elif couleurTirage == couleurMise :
        gain = math.ceil(mise/2)+mise
        print("""Vous gagnez la couleur : """, gain, """$""")
    else :
        print("""Vous avez perdu : """,mise)
        
    argent = argent + gain
    print("""il vous reste : """,str(argent) , "$")
    
    if argent == 0 :
        print("""Vous n'avez plus d'argent """)
        continuePartie = False
    else :
        sortirKO = True
        while sortirKO :
            sortir = input("Voulez vous continuer (Y) ou quitter le casino avec vos gains (N) ? " )    
            try :
                assert sortir == "Y" or sortir == "N"
                sortirKO = False
            except AssertionError :
                print("""Vous devez saisir Y ou N """)    
        if sortir == "N" :
            continuePartie = False

os.system("pause")


