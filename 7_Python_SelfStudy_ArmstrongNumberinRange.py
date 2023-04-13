# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:32:19 2023

@author: AJINKYA
"""

#Armstrong number in a range

#First of all take the lower limit from user 
lower = int(input("Enter a lower limit:"))

#Now take the upper limit from the user 

upper = int(input("Enter an upper limit"))

#Exception taken care of as per definitno of an Armstrong number 

if lower <= 0:
    raise Exception("Armstrong number can't be negative or zero. Please Enter a positive number.")

#Looping through the given range
for number in range (lower, upper+1):
    order = len(str(number)) #As power of each digit will be equal to the length of each digit. Hence, order calculated. 
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order 
        temp //= 10
    if sum == number:
        print(number)