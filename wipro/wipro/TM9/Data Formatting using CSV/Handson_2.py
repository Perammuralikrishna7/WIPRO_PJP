#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd

with open("income.csv",'w') as i:
    wr=csv.writer(i)
    wr.writerow(["ID","Fname","Lname","Salary"])
    while True:
        Id=input("Enter Id:")
        Fname=input("Enter first name of the employee:")
        Lname=input("Enter last name of the employee:")
        salary=input("Enter employees salary:")
        wr.writerow([Id,Fname,Lname,salary])
        option=input("Do you want to insert one more row[Yes/No] :")
        if option.lower()=='no':
            break
print("Total employees salary data written to csv")

