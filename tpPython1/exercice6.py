#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])
resultat = 1

print("calcul de la factorielle de " + str(n) + " : ")

if n==0 :
    print("1")
    exit()

for i in range(1,n+1):
    resultat*=i

print(resultat)


