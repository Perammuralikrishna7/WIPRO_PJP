#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))

try:
    num=n1//n2
except ZeroDivisionError:
    print("Invalid input")
else:
    print("Result ",num)

