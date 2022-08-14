#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("Enter a number:"))
count=0;
if n>1:
  for i in range(2,n):
    if(n%i == 0):
      print("Not prime number")  
      break  
  
  else: 
    print("prime number")    
else:
 print("Not prime number")  

