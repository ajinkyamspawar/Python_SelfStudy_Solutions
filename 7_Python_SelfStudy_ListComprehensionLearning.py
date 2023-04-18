# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:13:49 2023

@author: AJINKYA
"""

#List comprehenison learning

#Type1:

chhota_bhim = ["bhim", "Raju", "Kajri", "Golu"]

chhota_bhim_2 = [i.upper()for i in chhota_bhim]

print(chhota_bhim_2)

#Type2 :
    
list = [i for i in range(10)]

print(list)

#Type 3:


numbers = [1,2,3,4,5,6,7,8,9]

even_numbers = [i for i  in numbers if i % 2 == 0] #if we take range(len(numbers)) it will divide index and not the value. and will give index as output.


print(even_numbers)


#Type 4:
    
    