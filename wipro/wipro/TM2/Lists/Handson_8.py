#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list1=[]
length=int(input("Enter the length of the list:"))
#create a lsit
def createlist():
    while len(list1)<length:
        inp1=input()
        list1.append(inp1)
createlist()

#remove occurences
def remove_occurrence():
    Sub_list=[]
    for i in list1:
        if i not in Sub_list:
            Sub_list.append(i)
    return Sub_list
remove_occurrence()
print(remove_occurrence())

