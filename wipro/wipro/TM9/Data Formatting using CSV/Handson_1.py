#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['emp_name', 'dept', 'birth_month'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer.writerow(['James Carter','Marketing','February'])
    employee_writer.writerow(['Charu Palla','IT','March'])
    employee_writer.writerow(['Sahil Syed','Administration','January'])
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    

i_data=csv.reader('employee_file.csv')
i_data

