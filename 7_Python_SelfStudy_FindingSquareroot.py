# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:43:36 2023

@author: AJINKYA
"""

#Finding Squareroot 

# Method 1: Find out square root without using any in-built fucntion 

number = int(input("Enter a number to get its square root"))

squareroot = number**(0.5)

print("Square root of entered number is:",squareroot)


#Method 2: Using inbuilt function

import math 
number = int(input("Enter a number to get its square root"))

squareroot = math.sqrt(number)

print(squareroot)

