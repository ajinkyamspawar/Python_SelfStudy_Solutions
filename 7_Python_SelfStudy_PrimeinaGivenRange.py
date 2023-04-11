# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:46:10 2023

@author: AJINKYA
"""

lower = int(input("Enter lower limit of a number"))
upper = int(input("Enter Upper Limit of a number"))

for number in range (lower, upper+1):
    if number > 1: 
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            print(number)
            
            