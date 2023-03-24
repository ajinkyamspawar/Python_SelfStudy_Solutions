# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:08:52 2023

@author: AJINKYA
"""
#Q2: Write a python program to check whether a number is positive or not

#take the number as an input from user

number = int(input("Enter a number to check whether it is positive or negative"))

if number > 0: #number which is greater than zero is a positive number 
    print("Number",number,"is positive")
elif number < 0: #number which is less than zero is a negtive number
    print("Number",number,"is negative")
else: #number which is neither greater than zero nor less than, then it is zero.
    print("NUmber",number,"is neither positive nor negative, it is zero.")
