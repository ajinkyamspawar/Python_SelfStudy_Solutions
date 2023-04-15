# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 05:43:42 2023

@author: AJINKYA
"""

def factorial(n):
    if n == 0:
        return 1
    elif n==1:
        return 1
    else: 
        return (n * factorial(n-1))

n = int(input("Enter a number to get its factorial"))

print("Factorial of entered number is", factorial(n))
        
        