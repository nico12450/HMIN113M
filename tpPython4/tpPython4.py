#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import re

liste= []

connexions={}

#fd = open("last.txt","r")
#for ligne in fd.readlines():
#	liste.append(ligne)
#fd.close()

liste = os.popen("last")

for l in liste:
        #print(l)
        login = re.search("(^.+?)\s",l)
        if login:
                login = login.group(1)
        date=re.search("[A-Z][a-z]{2}.*?\d\d?",l)
        if date:
               date = date.group(0) 
        duree = re.search("\((\d{2})[\+:](\d{2}).?(.?.?)",l)
        dureeSep = ['0','0','']
        if duree:
        	dureeSep=[duree.group(1),duree.group(2), duree.group(3)]
        #print(dureeSep)
        #print(login)
        if login:
                #print(login)
                if login in connexions.keys():
                        if date:
                                #print(date)
                                if date in connexions[login].keys():
                                        if dureeSep[2]!='':
                                                #print(dureeSep[2])
                                                connexions[login][date]+= int(dureeSep[2])*24*60 + int(dureeSep[1]) +int(dureeSep[0])*60
                                        else:
                                                connexions[login][date] += int(dureeSep[1]) +int(dureeSep[0])*60
                                else:
                                        if dureeSep[2]!='':
                                                #print(dureeSep[2])
                                                connexions[login][date]= int(dureeSep[2])*24*60 + int(dureeSep[1]) +int(dureeSep[0])*60
                                        else:
                                                connexions[login][date] = int(dureeSep[1]) +int(dureeSep[0])*60
                else:
                        connexions[login] = {}
                        if date:
                                #print(date)
                                if date in connexions[login].keys():
                                        if dureeSep[2]!='':
                                                #print(dureeSep[2])
                                                connexions[login][date]+= int(dureeSep[2])*24*60 + int(dureeSep[1]) +int(dureeSep[0])*60
                                        else:
                                                connexions[login][date] += int(dureeSep[1]) +int(dureeSep[0])*60
                                else:
                                        if dureeSep[2]!='':
                                                #print(dureeSep[2])
                                                connexions[login][date]= int(dureeSep[2])*24*60 + int(dureeSep[1]) +int(dureeSep[0])*60
                                        else:
                                                connexions[login][date] = int(dureeSep[1]) +int(dureeSep[0])*60
                        

#print(connexions["reboot"]["Fri Oct 19"])

for k1 in connexions:
	print(k1)
	for k2 in connexions[k1]:
		print(k2)
                #print(connexions[k1][k2])

        
                        
                                        
        
                
                
