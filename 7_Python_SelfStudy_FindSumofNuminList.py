# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:49:38 2023

@author: AJINKYA

The code defines a list of integers called list, which contains ten elements.

The code sets a variable sum equal to 10, which is the sum that we want to find pairs for.

The code then uses a nested loop to iterate over all pairs of elements in the list.

For each pair of elements, the code checks if their sum equals the value of sum.

If the sum of the pair equals sum, the code prints the pair of elements.

The output of the program is a list of pairs of integers whose sum equals 10.
"""

#1)Method 1

list = [1,6,9,2,3,4,7,5,8,5]

sum = 10

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] + list[j] == sum:
            print("Pairs in list whose addition equals to given sum are as below:","(",  list[i], ",", list[j], ")") 
            print()
            
"Overall, the code is an implementation of the brute force approach to finding pairs of integers in a list that add"
" up to a given sum."
"The time complexity of the code is O(n^2) due to the nested loops, which makes it inefficient for large lists."


#------------------------------------------------------------------------------------------------------------------#
#Method 2
#Following and optimised approach

# Define the list of integers
lst = [1, 6, 9, 2, 3, 4, 7, 5, 8, 5]

# Define the target sum
target_sum = 11

# Create an empty set to store the complements of each element
complements = set()

# Iterate over the list of integers
for num in lst:
    complement = target_sum - num
    if complement in complements:
        print("Pairs in list whose addition equals to given sum are as below:", "(", num, ",", complement, ")")
    complements.add(num)
    
"In this version of the code, we use a set to store the complements of each element in the list. "
"We iterate over the list of integers and check if the complement of the current element is in the set of complements."
"If it is, we print the pair of elements whose sum equals the target sum. This approach has a time complexity of O(n),
" which is more efficient than the previous implementation."

          