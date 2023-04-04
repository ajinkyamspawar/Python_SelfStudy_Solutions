# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:54:37 2023

@author: AJINKYA
"""

#Checking if a string is a palindrome or not?

# Define a string variable
string = 'NITIN'

# Determine the length of the string
length_string = len(string)

# Initialize a checker variable to zero
checker = 0 

# Use a for loop to iterate over the range of the length of the string
for i in range(length_string):
    
    # Check if the character at the ith position in the string is not equal to the character at the 
    # (length of string - i - 1)th position
    if string[i] != string[length_string-i-1]:
        
        # If the above condition is true, set the checker variable to 1 and exit the loop
        checker = 1
        break
        
# Check the value of the checker variable and print the corresponding output
if checker == 0:
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")












#Alternative way by using slicing operator 
'''string = 'NITIN'

reverse_string = string[ : :-1]

if string == reverse_string:
    print("It is a palindrome")
else:
    print("It is not ia palindrome")'''
