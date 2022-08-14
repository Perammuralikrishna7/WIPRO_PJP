#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sys import argv

def checkPrime(e):
    count=0
    for i in range(2,e,11):
        if e%i==0:
            count+=1
    if count==0:
        return 1
    else:
        return 0
    
t=0
c=1
for j in range(1,11):
    n=int(argv[j])
    if n>1:
        if checkPrime(n)==1:
            t+=n
    elif n==1:
        t+=n
    else:
        pass
    c+=1

print(f"Total:{t}")

