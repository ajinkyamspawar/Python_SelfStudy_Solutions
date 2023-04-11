# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:00:13 2023

@author: AJINKYA
"""

#Find most repeated character in string

string = "dfhsdywegeyyyyyetwegrbweisdkiiiiii"

character = {}

for i in string:
    if i in character:
        character[i] += 1
    else:
        character[i] = 1
        
most_character = max(character, key=character.get)
print(character[i])
print(most_character)