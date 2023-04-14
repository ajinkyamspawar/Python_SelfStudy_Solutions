# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:57:54 2023

@author: AJINKYA
"""

def NNS(n):
    if n <= 1:
        return n
    else:
        return(n) + NNS(n-1)
    

n = int(input("Enter a number for range"))

if n<=0:
    print("Enter a positive number")
else: 
    print("The sum of natural numbers upto given numbers is:", NNS(n))