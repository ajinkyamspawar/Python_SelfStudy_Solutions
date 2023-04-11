# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:30:27 2023

@author: AJINKYA
"""

#Raising and exception 

# Define a list of integers
list = [1, 2, 3, 4]

# Initialize a variable to store the sum of the integers
sum = 0

# Loop over each integer in the list
for i in list:
    # If the integer is 1, raise an exception
    if i == 1:
        raise Exception("Exception 1 is found")
    # Otherwise, add the integer to the sum
    else:
        sum += i

# Print the sum of the integers in the list
print(sum)
