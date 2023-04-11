# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:30:31 2023

@author: AJINKYA
"""

#1) Fibonacci series using recursion

# Define a function that uses recursion to compute the nth Fibonacci number
def recursion_fibo(n):
    if n <= 1:
        return n
    else:
        return(recursion_fibo(n-1) + recursion_fibo(n-2))

# Prompt the user to input the number of Fibonacci terms to compute
nterms = int(input("Enter how many fibonacci terms you want: "))

# Check that the input is valid (i.e., positive)
if nterms <= 0:
    print("Please enter a positive number")
else: 
    # Compute and print the first nterms Fibonacci numbers using a loop
    for i in range(nterms):
        print(recursion_fibo(i))

        
#2) # Define a dictionary to store previously calculated Fibonacci numbers

memo = {0: 0, 1: 1}

def recursion_fibo(n):
    if n not in memo:
        memo[n] = recursion_fibo(n-1) + recursion_fibo(n-2)
    return memo[n]

# Prompt the user to input the number of terms to compute
try:
    nterms = int(input("Enter how many Fibonacci terms you want: "))
    if nterms <= 0:
        raise ValueError
except ValueError:
    print("Please enter a positive integer")
else:
    # Compute and print the first nterms Fibonacci numbers
    for i in range(nterms):
        print(recursion_fibo(i))
