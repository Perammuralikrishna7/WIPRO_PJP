#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range(10,99):
    if i>1:
        for n in range(2,i):
            if (i%n==0):
                break
        else:
            print(i)

