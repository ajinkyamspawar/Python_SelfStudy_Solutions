# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:40:01 2023

@author: AJINKYA
"""

#Displaying power of 2 using anonymous function: Method 1

power = int(input("Enter the limit of power"))

result = list(map(lambda x : 2**x, range(power+1)))

print(result)

#Same program using for loop: Method 2

power = int(input("Enter the limit of power"))

result = list(map(lambda x : 2**x, range(power+1)))

for i in range(power+1):
    print("The value of 2 raise to power", i, "is", result[i])
    