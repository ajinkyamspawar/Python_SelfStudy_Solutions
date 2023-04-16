# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:41:14 2023

@author: AJINKYA
"""

#Python program to merge dictionary 
#Method 1: Using / operator

dict1 = {"John":89, "Lisa":99}
dict2 = {"Lisa":94, "Peter":78}

print(dict1 | dict2)

#Method2: using ** operator

dict1 = {"John":89, "Lisa":99}
dict2 = {"Lisa":94, "Peter":78}

print({**dict1,**dict2})

#Method3: Using copy and update method
dict1 = {"John":89, "Lisa":99}
dict2 = {"Lisa":94, "Peter":78}

dict3 = dict2.copy()


dict3.update(dict1)

print(dict3)
