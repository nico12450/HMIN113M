#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) > 1 :
    
    print("il y'a " + str(len(sys.argv)-1) + "  paramètre")
    print("premier paramètre : " + sys.argv[1])

    if len(sys.argv) > 2:
        print("paramètres suivants : ")
        for p in sys.argv[2:] :
            print(p)
else :
    print("pas de paramètres")
