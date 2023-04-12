# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:48:26 2023

@author: AJINKYA
"""

#Sum on natural numbers till the limit of entered number 

number = int(input("Enter a number to get addition of natural numbers till it:"))
             
if (number <= 0):
    raise Exception("Only those numbers which are greater than 0 are natural numbers.")
else:
    sum = 0
    while number > 0:
        sum = sum + number
        number -= 1
    print(sum)