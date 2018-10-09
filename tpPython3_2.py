#!/usr/bin/env

import os,sys

dico = {}

def parcours(repertoire):
    
    print("je suis dans " + repertoire)
    liste = os.listdir(repertoire)

    for fichier in liste:
        
        if(os.path.isdir(fichier)):
            parcours(fichier)

        if(os.path.isfile(fichier)):

            cle = fichier.split(".")[-1]

            if(cle in dico.keys()):

                dico[cle] += 1

            else:

                dico[cle] = 1
            
            

chemin = sys.argv[1]
parcours(chemin)
