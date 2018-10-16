#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

connexions = {}

liste = os.popen("last")

for i in liste:

	#print(i)

	#print(len(i.split(" ")))

	#if(len(i.split(" ")) == 11):
	#	print(i.split(" ")[5])
	#elif (len(i.split(" ")) == 10):
	#	print(i.split(" ")[4])

	#print(i.split(" ")[0] + " " + i.split(" ")[4])

	r1 = re.search(".*?\s",i)
	r2 = re.search("[A-Z].*?\d\s",i)
	r3 = re.search("\((.*?):(.*?)\)",i)
	#print(r)
	print(r1.group(0))
	print(r2.group(0))
	print(r3.group(1))

          
print("fin")
