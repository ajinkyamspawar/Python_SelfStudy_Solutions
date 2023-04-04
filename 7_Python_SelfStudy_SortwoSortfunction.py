# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:33:15 2023

@author: AJINKYA
"""

#Sorting a list without using sort function 

#A list is created with unique numbers
list1 = [23, 45, 56, 32, 1, 1000, 999, 999.76]


#length of created list is calculated to use it as a range
length_list1 = len(list1)


#By using for loop we traverse the list for inspection 
#first for loop is used to take the element at ith position 
for i in range(length_list1):
    
    #second for loop is used to take the element at jth position 
    for j in range(i+1, length_list1):
        
        #elements at ith and jth postion are compared
        if list1[i] > list1[j]: 
            
        #if element at ith positon is greater than the element at jth position then we interchange their position
            list1[i],list1[j] = list1[j], list1[i]
            
#newly formed list is printed. 
print(list1)

'If a duplicate element is present in the list then it would not be taken out instead both the elements would be put in the list.'
'list[j]>list[i] will yield list in descending order.'