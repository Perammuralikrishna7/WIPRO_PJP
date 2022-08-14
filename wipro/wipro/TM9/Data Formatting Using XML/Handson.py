#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xml.etree.ElementTree as ET

tree=ET.parse('emp.xml')
root=tree.getroot()
for EmpNumber in root:
    print(EmpNumber.attrib['empno'])
    EmployeeNumber=EmpNumber.attrib['empno']
    for vals in EmpNumber:
        print(" ",vals.text)

