# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:11:34 2023

@author: AJINKYA
"""
#Counting number of vowels
#Method 1: Using dictionary
string = " Harry Potter and the goblet of fire"

vowels = "aeiou"

string = string.casefold()

print(string)

count = {}.fromkeys(vowels,0)

print(count)

for char in string:
    if char in count:
        count[char]+=1
print(count)


#Method 2: Using list and dictionary comprehension 
string = " Harry Potter and the goblet of fire"

vowels = "aeiou"

string = string.casefold()

count = {key: sum([1 for char in string if  char ==  key]) for key in vowels}

print(count)