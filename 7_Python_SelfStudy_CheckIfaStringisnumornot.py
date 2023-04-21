# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 22:21:11 2023

@author: AJINKYA
"""

num = input("Enter a number")

def float_check(num):
    try:
        float(num)
        return True
    except:
        return False

print(float_check(num))