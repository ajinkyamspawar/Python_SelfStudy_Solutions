# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:02:41 2023

@author: AJINKYA
"""

#Shuffling of cards:

import random, itertools

deck = list(itertools.product(range(1,14),['Spade','Club','Hearts','Diamond']))


random.shuffle(deck)



for i in range(4):
    print(deck[i][0],"of", deck[i][1])
    