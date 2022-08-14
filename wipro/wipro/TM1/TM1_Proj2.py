#!/usr/bin/env python
# coding: utf-8

# In[1]:


charge=0.51
fund=918
chargePerDay=charge*24
chargePerWeek=chargePerDay*7
chargePerMonth=chargePerDay*30
daysToOperate=fund/chargePerDay
print("How many days can i operate one server with? " + str(daysToOperate))
print("How much does it cost to operate one server perday? " + "$" +str(chargePerDay))
print("How much does it cost to operate one server perweek? " + "$" +str(chargePerWeek))
print("How much does it cost to operate one server permonth? " + "$" +str(chargePerMonth))

