# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:56:31 2023

@author: AJINKYA
"""
#Method 1: date time module
from datetime import datetime

date = "Mar 21 1993 11:39AM"

print(type(date))

date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")

print(date_time)
print(type(date_time))

#Method 2: dateutil module

from dateutil import parser

date_time = parser.parse("Mar 21 1993 11:39AM")

print(date_time)
print(type(date_time))