#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list1=[]
length=int(input("Enter the length of the list:"))
def createlist():
    while len(list1)<length:
        inp1=input()
        list1.append(inp1)
createlist()

def count_occurrences(list1,x):
    count=0
    for ele in list1:
        if (ele==x):
            count=count+1
    return count

print(li5)
print()
x=input("Enter an element to count it's occurence:")
print('{} has occurred {} times'.format(x,count_occurrences(li5,x)))

