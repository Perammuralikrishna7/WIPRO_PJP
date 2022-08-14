# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:12:37 2021

@author: ARAVIND
"""

from itertools import islice

n=int(input("Enter : "))

with open('sample2.txt') as f:
    for line in islice(f, n):
        print(line)