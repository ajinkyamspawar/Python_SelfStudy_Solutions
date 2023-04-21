# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 22:12:49 2023

@author: AJINKYA
"""

#Deleting an element from dictionary

#Method 1: Using delete keyword. 
marks = {"John": 89, "Lisa": 90, "Bob": 98, "harsh": 76}

print(marks)

del marks["John"]

print(marks)

#Method 2: Using pop function
marks = {"John": 89, "Lisa": 90, "Bob": 98, "harsh": 76}

pop_items = marks.pop("John")
print(marks)
