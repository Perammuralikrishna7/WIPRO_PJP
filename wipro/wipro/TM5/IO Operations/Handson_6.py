#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f1=open('sample1.txt','r')

str=f1.read()
li=str.split(' ')
print("frequency of words by user is ",len(li))
f1.close()

