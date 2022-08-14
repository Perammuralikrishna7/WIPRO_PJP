#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list1=["apples","Harry","banana","casting",]
list2=[14,15,"James","Hermoine","Justin Bieber"]
list1=list1[::-1]
list2=list2[::-1]
list2.extend(list1)
list2=list2[::-1]
print(list2)

