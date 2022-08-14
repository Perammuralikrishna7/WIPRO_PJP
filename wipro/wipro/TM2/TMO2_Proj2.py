#!/usr/bin/env python
# coding: utf-8

# In[ ]:


score_Sheet=[]

st_numbers=int(input("Enter number of participants:"))

for i in range(0,st_numbers):
    data=int(input())
    score_Sheet.append(data)
def secondmax(score_Sheet):
    sublist=[x for x in score_Sheet if x < max(score_Sheet)]
    return max(sublist)
if __name__ == '__main__':
    print("The Runner-up score is:",secondmax(score_Sheet))

