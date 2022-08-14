#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isPrime(n):
    p="The given number is a Prime number"
    np="The given number is not a Prime number"
    for i in range(2,n):
        if (n%i)==0:
            return np
        return p
n=int(input())
isPrime(n)

