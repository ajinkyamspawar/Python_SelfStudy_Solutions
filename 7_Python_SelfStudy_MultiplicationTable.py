# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:36:11 2023

@author: AJINKYA
"""

#Multiplication table

number = int(input("Enter a number to get it's table"))

for i in range(1,11):
    table = number * i
    print(table)
    print(number, "x", i, "=", table)
   
    
   
#Using recursion funciton method 1

def table(n, i=10):
    if i == 0:
        return
    table(n, i-1)
    print(n * i)
    

number = int(input("Enter a number to get its table: "))
table(number)


#Table using recursion but in reverse order ????
def table(n, i=1):
    if i == 11:
        return
    table(n, i+1)
    print(n * i)
    

number = int(input("Enter a number to get its table: "))
table(number)


#Using recursion function method 2
def table(n, i=1):
    # Base case: if i reaches the upper limit, stop the recursion
    if i == 11:
        return
    
    # Print the current value of n multiplied by the current index
    print(n * i)
    
    # Recursively call the function with the next index
    table(n, i+1)

# Ask the user for input and call the function with the user's number as input
number = int(input("Enter a number to get its table: "))
table(number)

#Using while loop:

n =7 
i =1 
while i<=10:
    print(n, "x", i, "=", n*i)
    i += 1