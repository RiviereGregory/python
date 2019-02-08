# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:43:39 2019

@author: Greg13
"""

import os

annee = input("saisie une année : " )
annee = int(annee)
bissextile = False

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
    
os.system("pause")