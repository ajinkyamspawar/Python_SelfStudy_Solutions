# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 18:18:49 2023

@author: AJINKYA
"""

#Q3:Write a program to take in marks of 5 subjects and display their grades.

#take the input of 5 subject marks from student
print("Enter marks of 5 subjects")

#converting the taken input into integer format and then storing them in respectve variables

sub1 = float(input())
sub2 = float(input())
sub3 = float(input())
sub4 = float(input())
sub5 = float(input())

#taking the average of all subject marks 

average = ((sub1+sub2+sub3+sub4+sub5)/5) 

print("Average is:",average)

#Deciding the grades based on marks. 
if average < 35:
    print("You are Fail")
elif average >= 35 and average < 50:
    print("You are Pass")
elif average >= 50 and average < 75:
    print("You got First class")
else:
    print("Yuhoo! Distinction")
