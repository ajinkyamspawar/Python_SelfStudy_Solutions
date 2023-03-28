# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:00:33 2023

@author: AJINKYA

"""

#Q1 Swap values of 3 variable without taking a temporary variable 
# Assign 3 values to 3 different variables
a = 10
b = 20
c = 30
print("Values before swapping:","a=",a,"b=",b,"c=",c)
#Swapping the values of these three variables 

a,b,c = c,a,b

print("Values after swapping:","a=",a,"b=",b,"c=",c)
