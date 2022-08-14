#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=input()
if s[0]=="x" and s[len(s)-1]:
    c=s[1:len(s)-1]
    print(c)
else:   
    print(s)

