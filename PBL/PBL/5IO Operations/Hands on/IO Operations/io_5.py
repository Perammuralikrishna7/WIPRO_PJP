# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:27:21 2021

@author: ARAVIND
"""

def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_words('sample.txt'))