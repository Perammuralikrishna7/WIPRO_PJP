#!/usr/bin/env python
# coding: utf-8

# In[4]:


n1=int(input("Enter a number n1: "))
n2=int(input("Enter a number n2: "))

if (n1 >= 0 and n2  >= 0) :
    if ((n1%10)==(n2%10)):
        print("True")
    else:
        print("False")
else:
    print("The given numbers are not non-negatvie values")


# In[ ]:




