# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:36:28 2021

@author: ARAVIND
"""

from collections import Counter

with open('sample2.txt') as f:
    print(Counter(f.read().split()))


