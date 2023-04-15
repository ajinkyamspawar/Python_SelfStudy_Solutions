# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 11:52:35 2023

@author: AJINKYA
"""

#Transpose of a Matrix: 
#Method 1: Using for loop with use of nested loop concept

A = [[1,2,3], [4,5,6]]

B = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        B[j][i] = A[i][j]
for i in B:
    print(i)

#Method 2: Using list comprehension

A = [[1,2,3], [4,5,6]]

T = [[A[j][i] for j in range(len(A)) ] for i in range(len(A[0]))]

for i in T:
    print(i)