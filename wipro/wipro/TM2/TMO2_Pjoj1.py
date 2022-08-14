#!/usr/bin/env python
# coding: utf-8

# In[1]:


dic=dict()


# In[ ]:


cont=input("Press 1 to update or enter a new person & Press 2 print message for existing perons:")
print(dic)
print('\n')
if cont=='1' or cont=='2':
    if cont=='1':
        if len(dic)==0:
            people=input("Enter a name:")
            fact=input("Enter a fact:")
            dic[people]=fact
        else:
            name1=input("Enter a name:")
            if name1 in dic:
                def updateMessage(people,fact):
                    fact=input("Enter the fact:")
                    dic[people]=fact
                updateMessage(people,fact)
            else:
                people=input("Enter a name:")
                fact=input("Enter a fact:")
                dic[people]=fact
        print(dic)
    else:
        for key, value in dic.items():
            msg=input("Enter a message:")
            msg1=f'{key}: {msg} {value}'
            print('\n',msg1)
            print('\n')
else:
    print("Invalid")

