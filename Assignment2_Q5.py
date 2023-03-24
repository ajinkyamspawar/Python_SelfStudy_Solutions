# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:32:30 2023

@author: AJINKYA
"""

#Q5: Write a program to find out maximum number from given numbers 

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

if num1 > num2:
    if num1 > num3:
        print("Num1 i.e.", num1, "is the greatest number among three numbers.")
    else:
        print("Num3 i.e.", num3, "is the greatest number among three numbers.")
elif num2 > num3:
    print("Num2 i.e.", num2, "is the greatest number among three numbers.")
else: 
    print("Num3 i.e.", num3, "is the greatest number among three numbers.")
    
''' 
One more way usinng built-in max function: 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

max_num = max(a, b, c)

print("Maximum number is:", max_num)

In this program, we first prompt the user to enter three numbers using the input function and convert them to integers using the int function. We then use the built-in max function to find the maximum of the three numbers and assign it to the variable max_num. Finally, we print out the result using the print function.
'''