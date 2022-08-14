#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n1=int(input("Enter a number:"))

n2=n1

sum=0
while(n1>0):
    ld=n1%10
    sum=(sum*10)+ld
    n1=n1//10
    
if (n2==sum):
    print(n2,"is a Palindrome")
else:
    print(n2,"is not a Palindrome")

