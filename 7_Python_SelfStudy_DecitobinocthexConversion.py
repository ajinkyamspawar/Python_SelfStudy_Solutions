# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:38:05 2023

@author: AJINKYA
"""

#Converting Decimal to binary, octal, hexadecimal 

#Taking the value of input:
decimal = int(input("Enter a number to convert it:"))

#We will use built-in functions in python:
    
print("The converted value of", decimal, "is:")
print(bin(decimal), "in binary")
print(oct(decimal), "in octal")
print(hex(decimal), "in hexadecimal")
