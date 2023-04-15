# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 11:21:21 2023

@author: AJINKYA
"""
#Method 1: This program is written only for positive numbers conversion. 

def convertbinary(n):
    if n > 1:
        convertbinary(n//2)
    print(n%2, end = "")

convertbinary(4)

#Method 2: This program is written for decimal integers conversion into binary.

def decimal_to_binary(num):
    if num >= 0:
        if num == 0:
            return '0'
        else:
            return decimal_to_binary(num // 2) + str(num % 2)
    else:
        return '-' + decimal_to_binary(-num)
decimal_to_binary(10)

decimal_to_binary(-10)

decimal_to_binary(0)
