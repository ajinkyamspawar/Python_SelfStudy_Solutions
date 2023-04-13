# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:02:34 2023

@author: AJINKYA
"""

number = int(input("Enter a number to check whether it is armstrong or not:"))
order = len(str(number))

sum = 0
temp = number 

while temp > 0:
    digit = temp % 10
    sum += digit ** order 
    temp //= 10
    
if sum == number:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
    
#1,2,3,4,5,6,7,8,9, 153. 1634, 4210818
    