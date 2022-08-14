#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("Enter no of line to read "))
f1=open('sample.txt','r')
for i in range(1,n+1):
    print(f1.readline())


f1.close()

