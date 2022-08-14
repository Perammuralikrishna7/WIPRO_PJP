#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def countUpperLower():
    up=0
    low=0
    for i in inp1:
        if (i.isupper()):
            up=up+1
        else:
            low=low+1
    print("Upper case letters are",up)
    print("lower case letters are",low)
inp1=input()
countUpperLower()

