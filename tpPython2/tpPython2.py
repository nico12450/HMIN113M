#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
import sys

fd = open("capitales.csv","r")
pays = []
capitales = []

for ligne in fd:
    #print(ligne, end = " ")
    data = ligne.split(",")
    pays.append(data[0])
    capitales.append(data[1].strip())
    
#print(pays,capitales)

fd.close()

longueur = len(pays)
continuer = True
inverse = len(sys.argv) > 1
nbBonnesReponses = 0
nbReponses = 0
paysDemandes = []

#indiceAlea = randint(0,longueur)

#print (pays[indiceAlea],capitales[indiceAlea])

while(continuer and not inverse):
        
        indiceAlea = randint(0,longueur)

        if(pays[indiceAlea] in paysDemandes):
            continue
        
        print("quelle est la capitale de " + pays[indiceAlea] + " ?")

        if(input().upper() == capitales[indiceAlea].upper()):
            print("bonne réponse")
            nbBonnesReponses += 1

        else:
            print("mauvaise réponse")
            print("la bonne réponse était : " + capitales[indiceAlea])

        nbReponses +=1

        paysDemandes.append(pays[indiceAlea])

        print("continuer ? o/n")

        if(input() == "n"):
            continuer = False
            print("fin de la partie")
            print(str(nbBonnesReponses) + " bonnes réponses")
            print(str(nbReponses-nbBonnesReponses) + " mauvaises réponses")
            #print(str(nbBonnesReponses) + " / " + str(nbReponses))
            print(str((nbBonnesReponses/nbReponses) * 100) + "% de bonnes réponses")

continuer = True
            
while(continuer and inverse):
        
    indiceAlea = randint(0,longueur)

    if(pays[indiceAlea] in paysDemandes):
        continue
        
    print("quel est le pays de :  " + capitales[indiceAlea] + " ?")

    if(input().upper() == pays[indiceAlea].upper().split(" (")[0]):
        print("bonne réponse")
        nbBonnesReponses += 1

    else:
        print("mauvaise réponse")
        print("la bonne réponse était : " + pays[indiceAlea].split(" (")[0])

    nbReponses +=1

    paysDemandes.append(pays[indiceAlea])

    print("continuer ? o/n")

    if(input() == "n"):
        continuer = False
        print("fin de la partie")
        print(str(nbBonnesReponses) + " bonnes réponses")
        print(str(nbReponses-nbBonnesReponses) + " mauvaises réponses")
        #print(str(nbBonnesReponses) + " / " + str(nbReponses))
        print(str((nbBonnesReponses/nbReponses) * 100) + "% de bonnes réponses")
