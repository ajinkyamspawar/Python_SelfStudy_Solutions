# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:42:44 2023

@author: AJINKYA
"""

#Factorial using recursion 

def fact(n):
    if n == 0:
        return 1
    elif n <0:
        raise Exception("Factorial of negative number does not exist")
    else:
        return (n * fact(n-1))





number = int(input("Enter a number to get its factorial"))

result = fact(number)

print(result)