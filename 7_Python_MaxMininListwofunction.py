# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:08:46 2023

@author: AJINKYA
"""

#Find the maximum and minimum number in a list without using function 

#Method 1 
# Define a list of integers
list = [12, 74, 4, 3, 342, 3423]

# Set the initial values of maximum and minimum to the first element of the list
maximum = list[0]
minimum = list[0]

# Loop over each element in the list
for i in list:
    # If the current element is greater than the current maximum, update the maximum
    if i > maximum:
        maximum = i
    # If the current element is less than the current minimum, update the minimum
    elif i < minimum:
        minimum = i

# Print the maximum and minimum values
print("maximum:", maximum)
print("minimum:", minimum)




#Method 2 
list = [12, 74, 4, 3, 342, 3423]

maximum = None
minimum = None

for i in list:
    if maximum is None or i > maximum:
        maximum = i
    if minimum is None or i < minimum:
        minimum = i

print("maximum:", maximum)
print("minimum:", minimum)


''' O(n) This code has the same time complexity as the original code, but it performs fewer comparisons
 in cases where the initial values of maximum and minimum are not in the middle of the range of values in the list.'''





#using a function 

list1 = [12, 74, 4, 3, 342, 3423]

list2 = sorted(list1)

print(list2)
print(list2[0], list2[-1])