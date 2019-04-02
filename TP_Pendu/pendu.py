# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:03:46 2019

@author: Greg13
"""

from donnees import *
from fonctions import *

scores = recupScores()
utilisateur = recupNomUtilisateur()

if utilisateur not in scores.keys():
    scores[utilisateur] = 0

continuerPartie = 'o'

while continuerPartie != 'n':
    print("Joueur {0}: {1} point(s)".format(utilisateur, scores[utilisateur]))
    motATrouver = choisirMot()
    lettresTrouvees = []
    motTrouve = recupMotMasque(motATrouver, lettresTrouvees)
    nbChances = nbCoups
    while motATrouver!=motTrouve and nbChances>0:
        print("Mot à trouver {0} (encore {1} chances)".format(motTrouve, nbChances))
        lettre = recupLettre()
        if lettre in lettresTrouvees: 
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in motATrouver: 
            lettresTrouvees.append(lettre)
            print("Bien joué.")
        else:
            nbChances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")
        motTrouve = recupMotMasque(motATrouver, lettresTrouvees)

    if motATrouver==motTrouve:
        print("Félicitations ! Vous avez trouvé le mot {0}.".format(motATrouver))
    else:
        print("PENDU !!! Vous avez perdu.")

    scores[utilisateur] += nbChances

    continuerPartie = input("Souhaitez-vous continuer la partie (O/N) ?")
    continuerPartie = continuerPartie.lower()

enregistrerScores(scores)

print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))
