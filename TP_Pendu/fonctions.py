# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:03:28 2019

@author: Greg13
"""
import os
import pickle
from random import choice

from donnees import *

# Scores

def recupScores() :
    if os.path.exists(nomFichierScores) :
        with open(nomFichierScores ,'rb') as fichierScores :
            monDePikler = pickle.Unpickler(fichierScores)  
            scores = monDePikler.load()
    else:
        scores = {}
    return scores

def enregistrerScores(scores) :
    with open(nomFichierScores,'wb') as fichierScores :
        monPikler = pickle.Pickler(fichierScores)  
        monPikler.dump(scores)
    
def recupNomUtilisateur():
    nomUtilisateur = input("Tapez votre nom: ")
    nomUtilisateur = nomUtilisateur.capitalize()
    if not nomUtilisateur.isalnum() or len(nomUtilisateur)<4:
        print("Ce nom est invalide.")
        return recupNomUtilisateur()
    else :
        return nomUtilisateur
    
def recupLettre():
    lettre = input("Tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return recupLettre()
    else :
        return lettre
    
def choisirMot():
    return choice(listeMots)

def recupMotMasque(motComplet, lettresTrouvees):
    motMasque = ""
    for lettre in motComplet:
        if lettre in lettresTrouvees:
            motMasque += lettre
        else:
            motMasque += "*"
    return motMasque
    
            



