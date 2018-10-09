#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,sys
#from copy import deepcopy

dico = {'pasdesuffixe':0}
chemin = ""

if (len(sys.argv) == 1):
        chemin = os.getcwd()
else:       
        chemin = sys.argv[1]

def parcours(repertoire):
        
    print("je suis dans " + repertoire)
    liste = os.listdir(repertoire)

    for fichier in liste:
        cheminLocal = repertoire + "/" + fichier

        print(fichier + str(os.path.isfile(cheminLocal)))

        if(os.path.isdir(cheminLocal)):
            parcours(cheminLocal)
            #print("c'est un répertoire")

        if(os.path.isfile(cheminLocal)):

            cle = fichier.split(".")[-1]

            if(len(fichier.split("."))==1):
                    cle = "pasdesuffixe"
            
            print(cle)

            if(cle in dico.keys()):

                dico[cle] += 1

            else:

                dico[cle] = 1
        
parcours(chemin)

for (extension, nombre) in dico.items():
        print(extension + " : " + str(nombre))
