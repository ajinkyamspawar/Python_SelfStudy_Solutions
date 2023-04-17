# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:42:29 2023

@author: AJINKYA
"""

#Python Program to sort a dictionary by value

# Method 1:
    
mahabharat = {"Krishna" : 1 , "Karna":7, "kunti": 4, "Eklavya": 11, "Bhisma": 2}
#dictionary doesn't contain indexing but keys stand at certain indexes. 

sv = sorted(mahabharat.items(), key = lambda x : x[1]) #1 written to sort by using value

print(sv)

#Method 2: Sort on the basis of keys:
sv = sorted(mahabharat.items(), key = lambda x : x[0]) #0 written to sort by using value

print(sv)

#Method 3: Sort only the values:
    
v = sorted(mahabharat.values())# As values is a function it needs paranthesis
print(v)


