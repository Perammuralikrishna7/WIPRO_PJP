#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=input()
u=0
l=0
for i in s:
    if (i.isupper()):
        u=u+1
    elif (i.islower()):
        l=l+1
print("upper",u)
print("lower",l)

