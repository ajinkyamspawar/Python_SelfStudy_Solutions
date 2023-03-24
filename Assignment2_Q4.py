# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:58:22 2023

@author: AJINKYA
"""

#Q4: Write a program to take input from user and print the sum of x+xx+xxx

print("Enter a number to get it sum in x+xx+xxx format") #The user is prompted to enter a number.

n = int(input()) #The input is converted to an integer and stored in the variable n.

nn = int(str(n) + str(n)) #nn is calculated by concatenating n with itself as a string using the str() function,
                          #then converting the result back to an integer using the int() function.

nnn =  int(str(n) + str(n) + str(n) )

                    #nnn is calculated by concatenating n with itself twice as a string using the str() function, 
                    #then converting the result back to an integer using the int() function.

#The sum of n, nn, and nnn is stored in the variable result.
result = int(n)+int(nn)+int(nnn) 

#The result is printed to the console using the print() function.

print(n,"+",n,n,"+",n,n,n,"=",result)