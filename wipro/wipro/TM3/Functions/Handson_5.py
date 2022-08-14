#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def createlist(lis,length):
    while len(lis)<length:
        inpt=int(input())
        lis.append(inpt)

def EvenIn_list():
    for i in lis:
        if (i%2==0):
            lis1.append(i)
    return lis1

lis=[]
lis1=[]
length=int(input())
createlist(lis,length)
EvenIn_list()

