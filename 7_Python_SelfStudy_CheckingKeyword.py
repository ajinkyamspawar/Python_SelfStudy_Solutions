# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:48:44 2023

@author: AJINKYA
"""

import keyword

list = ["Ram","continue", "Laxman","Seetha","break", "if"]

for i in range (len(list)):
    if keyword.iskeyword(list[i]):
        print(list[i], ":It is a keyword in Python")
    else:
        print(list[i], "is Hindu god's name.")
        
