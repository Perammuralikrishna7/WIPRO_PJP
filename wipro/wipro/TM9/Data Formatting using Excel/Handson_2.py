#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#-->writing data in excel
import openpyxl as pyxl

from openpyxl import Workbook
s=Workbook()
s['Sheet'].title=("Employee data")
sh1=s.active
sh1['A1'].value='EmpNo'
sh1['B1'].value='Name'
sh1['C1'].value='Salary'
sh1['A2'].value=input("Enter Employee ID:")
sh1['B2'].value=input("Enter name:")
sh1['C2'].value=input("Enter Salary:")
sh1['A3'].value=input("Enter Employee ID:")
sh1['B3'].value=input("Enter name:")
sh1['C3'].value=input("Enter Salary:")
sh1['A4'].value=input("Enter Employee ID:")
sh1['B4'].value=input("Enter name:")
sh1['C4'].value=input("Enter Salary:")

#-->Saving
s.save("employee.xlsx")

