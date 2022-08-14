#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list1=[]
def createlist():
    while len(list1)<5:
        inp1=input()
        list1.append(inp1)
    print(list1)
createlist()
print()
for i in list1:
    print(int(i))

