# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:25:49 2023

@author: AJINKYA
"""
#Dispalying values in a dictionary 
#Method 1: using .items()
dict = {1:"Yudhisthir", 2:"Bhim", 3:"Arjun",4:"Nakul", 5:"Sahdev"}

print(dict[1])

for key, value in dict.items():
    print(key, "-", value)


#Method 2: 
    
for key in dict:
    print(key, ":", dict[key])

#Method 3:

for key in dict.keys():
    print(key)
    print(dict[key])
    
#Method 4:
for value in dict.values():
    print(value)
     