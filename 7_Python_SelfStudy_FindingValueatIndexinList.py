# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:32:46 2023

@author: AJINKYA
"""

#Program to find out value at index,

#Method 1: Using enumerator

list = [23,24,56,78,80,10]

for index, value in enumerate(list):
    print(index, value)
    

##ethod 2: Use of for loop without enumerate:
list = [23,24,56,78,80,10] 

for index in range(len(list)):
    value = list[index]
    print(index, value)
    
    