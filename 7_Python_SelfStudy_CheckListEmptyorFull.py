# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:02:27 2023

@author: AJINKYA
"""

#Python program to check if a list is empty or not! 

#Method 1: Using boolean operator
list1 = [1,2,3,4,5]

list2 = []

print(bool(list1))
print(bool(list2)) 

#Method 2: Using boolean 2nd method
if not list1:
    print("List is empty")
else:
    print("List has elements")
    
if not list2:
    print("List is empty")
else:
    print("List has elements")
    
    
#Method 3: Using len operator

if len(list1) == 0:
    print("List is empty")
else:
    print("List is full")

if len(list2) == 0:
    print("List is empty")
else: 
    print("List is full")
    
#Method 4: using square brackets

if list1 == []:
    print("List is empty")
else:
    print("List is full")

if list2 == []:
    print("List is empty")
else: 
    print("List is full")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    