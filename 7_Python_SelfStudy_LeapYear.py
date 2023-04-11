# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:16:41 2023

@author: AJINKYA
"""

#Checking entered year is a leap year or not

year = int(input("Enter year to check whether it is leap or not:"))

if (year % 400 == 0) and (year % 100 == 0):
    print(year, " year is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, " year is a leap year")
else:
    print(year, "year is not a leap year.")