#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])

print("calcul des nombres premiers contenus entre 0 et " + str(n))

def testPremier(nombre):
    for i in range(2,nombre):
        if nombre%i == 0:
            return False
    return True

def calculPremiers(limite):
    listePremiers = []
    for i in range(1,limite+1):
        if testPremier(i):
            #print(i)
            listePremiers.append(i)
    return listePremiers
    
print(calculPremiers(n))

def calculNPremiers(N):
    
    listeNPremiers = []
    i = 1
    
    while len(listeNPremiers) < N:
        if testPremier(i):
            listeNPremiers.append(i)
        i+=1

    return listeNPremiers

print("calcul des " + str(n) + " premiers nombres premiers")
print(calculNPremiers(n))

    


