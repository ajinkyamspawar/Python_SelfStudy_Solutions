# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:00:33 2023

@author: AJINKYA
"""

#Learninig Iterators: 

#Method 1:    
list = [1,2,3,4,5,6]

iterate = iter(list)

print(iterate.__next__())
print(iterate.__next__())
print(next(iterate))

#Method 2: 

    
String = "Ajinkya Pawar"

iterate  = iter(String)

print(iterate.__next__())
print(next(iterate))

#Method 3: Creating own iterator: #this code did not run in spyder but succeful run in PyCharm
    
class TheDarkKnight:
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.num<=5:
            value = self.num
            self.num+=1
            return value
        else:
            raise StopIteration
TDK = TheDarkKnight()

for i in TDK:
    print(i)