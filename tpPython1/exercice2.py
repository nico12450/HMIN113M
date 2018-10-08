#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) > 1 :
    print("il y'a " + str(len(sys.argv)-1) + "  paramètre")
else :
    print("pas de paramètres")
