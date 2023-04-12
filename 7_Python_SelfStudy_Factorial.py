# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:07:53 2023

@author: AJINKYA
"""

#Taking input from user 

number = int(input("Enter a number to get it's factorial"))

# Intializing fact variable at 1 to traverse till the number 
fact = 1

# looping through the range
for i in range(1, number+1):
    fact = fact * i

#Printing factorial
print(fact)


# One more method 


number = int(input("Enter a number to get it's factorial"))


fact = 1

while i !=0:
    fact = fact * number
    number -= 1
print(fact)


    
    