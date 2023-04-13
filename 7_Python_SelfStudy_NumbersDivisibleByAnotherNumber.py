# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:06:03 2023

@author: AJINKYA
"""

#Finding numbers in a range divisble by entered or hard coded number or not?
#Method 1: Using for loop:

for i in range(1,100):
    if i % 13 == 0 :
        print(i)
        
#Method 2: Using anonymous fucntion i.e. lambda 

l = [12, 27, 39, 53, 54, 79, 90, 91]

result = list(filter(lambda x : x % 13 == 0, l))

print(result)

#Method 3: Input from user, using for loop:
number = int(input("Enter which number you want to check"))
for i in range(1,100):
    if i % number == 0 :
        print(i)

#Method 4: input from user for lambda function: 

number = int(input("Enter which number you want to check"))    

#l = [12, 27, 39, 53, 54, 79, 90, 91] or by using for loop as follows:
# result = list(filter(lambda x : x % number == 0, l))

result = list(filter(lambda x: x % number == 0, range(1,100)))
              
print(result)
