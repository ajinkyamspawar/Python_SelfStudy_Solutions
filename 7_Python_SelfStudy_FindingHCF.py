# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:21:41 2023

@author: AJINKYA
"""

#Method 1; Finding HCF of a number
#A function is created
def findHCF(x,y):
    if x > y: #smaller number is found out as it hcf can't be grater than the smallest number
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1): #Range is set 
        if ((x % i == 0) and (y % i == 0)): #both the conditions needs to be true
            hcf = i
    return hcf 

print("The HCF of a number is:", findHCF(12,30))

#Method 2: Finding HCF of number from 3 numbers

def findHCF(x,y,z):
    if x<y:
        if x<z:
            smaller = x
        else: 
            smaller = z
    if y<z: 
        smaller = y
    else: 
        smaller = z
    for i in range(1,smaller+1):
        if( (x%i == 0) and (y%i == 0) and (z%i == 0)):
            hcf = i
    return hcf

print("The HCF of a number is:", findHCF(10,30,20))