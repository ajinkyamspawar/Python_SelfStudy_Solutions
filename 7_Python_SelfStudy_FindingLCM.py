# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:34:44 2023

@author: AJINKYA
"""
#Method 1: Finding LCM without using in-built function 
def findLCM(x,y):
    for i in range(1, 1000): #Range is set , As the range can't be predefined  we can take user input too and assign it as upper limit.
        v1 = x*i
        for j in range(1,1000):
            v2 = y*j  
            if v1 == v2:
                lcm= v1 = v2
                return lcm 

print("The LCM of a number is:", findLCM(6,10))


#Method 2: Optimized program using in-built function
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

print("The LCM of a number is:", lcm(6, 10))
