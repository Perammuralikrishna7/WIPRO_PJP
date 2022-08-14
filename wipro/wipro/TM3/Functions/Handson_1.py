#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def createlist(l,leng):
    while len(l)<leng:
        inp=int(input())
        l.append(inp)

def SumOfList():
    s=0
    for i in l:
        s=s+int(i)
    return s

l=[]
leng=int(input())
createlist(l,leng)
SumOfList()

