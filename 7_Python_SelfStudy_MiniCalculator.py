# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:00:51 2023

@author: AJINKYA
"""

#Program to make a simple calculator

print("~~~~~MINI CALCULATOR~~~~~")


num1 = int(input("Input first number"))



print("Enter 1 for additon/n Enter 2 for subtraction /n Enter 3 for multiplication /n Enter 4 for division.")
choice = int(input())

num2 = int(input("Input second number"))


print("Result is:")
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("Invalid input")
