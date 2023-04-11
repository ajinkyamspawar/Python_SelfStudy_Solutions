# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:24:06 2023

@author: AJINKYA
"""

number = int(input("Enter a number to check whether it is prime or not"))

if number <= 1:
    raise Exception("Enter a value greater than 1 as  By definition, a prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.")
    
if number > 1:
    for i in range(2, number):
        if (number % i == 0):
            print("Number is not prime")
            break
    else:
        print("It is a prime number")

    