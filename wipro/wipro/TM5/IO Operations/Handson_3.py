#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=input("Enter text that to be added in file ")

f1=open('sample.txt','a')
f1.write(n)

f1.close()

