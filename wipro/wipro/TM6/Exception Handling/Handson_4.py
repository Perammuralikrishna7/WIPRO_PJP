#!/usr/bin/env python
# coding: utf-8

# In[ ]:


li=[1,2,3,4,5,-6,-9,10,22,60]

try:
    n=int(input("Enter the index to find "))
    if li[n]>0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Not a valid index")

