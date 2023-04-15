# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:11:55 2023

@author: AJINKYA
"""

string = "The quick brown fox jumps over the fence"
#Need to split it first
split_string = string.split()

print(split_string)
#convert it to lower case to standardise it
for i in range(len(split_string)):
    split_string[i] = split_string[i].lower()

print(split_string)

#now sort it
split_string.sort()

print(split_string)


