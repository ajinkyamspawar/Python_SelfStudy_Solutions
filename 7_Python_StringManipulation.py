# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:13:20 2023

@author: AJINKYA
"""

#String Manipulation:

#Method 1
str1 = "$%You @ r#@!oc$k % the * world!"

str2 = ' '

for i in str1:
    if ((i>='A' and i<='Z') | (i>='a' and i<='z') | (i == '')):
        str2 = str2+i
        
print(str2)





#Method 2 Reversing the string 

str1 = "You are my blue-eyed boy"

l = str1.split()

print(l) # used to print to understand how .split works 

l = l[::-1]

print(l)

l =''.join(l)

print(l)


#Outputs for Method 2
'''
['You', 'are', 'my', 'blue-eyed', 'boy']
['boy', 'blue-eyed', 'my', 'are', 'You']
boyblue-eyedmyareYou

'''

# Food for thought 
s = "Hello"

s = "Hello" + s[0:1]
print(s)
