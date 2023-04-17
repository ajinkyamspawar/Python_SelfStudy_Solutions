# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:18:13 2023

@author: AJINKYA
"""

#Python program to catch multiple extensions in one line:
    
#When an error comes in a program it stops its execution. To avoid this and to run program without break we use exception handling.

name = input("Enter your name:")

try:
    rollno = int(input("Enter your roll no:"))

    print(name + rollno)
except (TypeError, ValueError) as a:
    print(a)
print("Thank You")