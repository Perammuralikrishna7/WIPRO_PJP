#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num=int(input("Enter a number:"))

sum=0
while(num>0):
    ld=num%10
    sum=(sum*10)+ld
    num=num//10
    
print("The reverse number is:",sum)

