# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:15:29 2023

@author: AJINKYA

The code sorts the keys of dict1 using the sorted() function and then creates a new dictionary 
dict2 with the same key-value pairs as dict1, but with the keys sorted in ascending order.


"""

# A new unsorted dictionary is created 
dict1 = {981:"Seeta", 456:"geeta", 765:"Babita", 876:"Lalita"}

# Sort the keys of dict1
dict_sorted_key = sorted(dict1.keys())

# Create a new dictionary dict2 and copy the key-value pairs from dict1 to dict2 in sorted order 

dict2 = {}
#The for loop copies the key-value pairs from dict1 to dict2 in sorted order.
for i in dict_sorted_key:
    dict2[i] = dict1[i]

# Print the new dictionary dict2
print(dict2)


"""
The same code can be optimised in the following ways:
    
1) Using dictionary comprehension 
    
    dict1 = {981:"Seeta", 456:"geeta", 765:"Babita", 876:"Lalita"}

    # Create a new dictionary dict2 with the same key-value pairs as dict1, but with the keys sorted in ascending order
    dict2 = {k: dict1[k] for k in sorted(dict1)}

    # Print the new dictionary dict2
    print(dict2)
    
2) using dict comprehension and lambda function 
    
  # A new unsorted dictionary is created 
  dict1 = {981:"Seeta", 456:"geeta", 765:"Babita", 876:"Lalita"}  
  
  dict2 = {key:value for key, value in sorted (dict1.items(), key = lamda x:x[1])}
  
  print(dict2)
"""