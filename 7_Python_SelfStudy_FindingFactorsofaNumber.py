# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:57:48 2023

@author: AJINKYA
"""

#Program to find factors of a number: 

number = int(input("Enter a number to get its factors."))

for i in range(1, number+1):
    if number % i == 0:
        print(i)