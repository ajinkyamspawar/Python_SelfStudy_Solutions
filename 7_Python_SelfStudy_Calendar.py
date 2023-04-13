# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:31:59 2023

@author: AJINKYA
"""

import calendar, random 

year = int(input("Enter year"))
month = int(input("Enter month"))

calendar = calendar.month(year,month)
#random.calendar()
print(calendar)
