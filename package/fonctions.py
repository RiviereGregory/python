# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:28:04 2019

@author: Greg13
"""
import os

def table(nb, max=10):
    i = 1
    while i <= max :
        print(i , "*" ,nb," = ",i*nb )
        i += 1
        
# test de la fonction table

if __name__ == "__main__":
    table(4)
    os.system("pause")