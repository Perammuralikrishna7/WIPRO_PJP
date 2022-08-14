def countAlp(str):
   u=0
   l=0
   for i in str:
      if (i.isupper()):
          u=u+1
      elif (i.islower()):
          l=l+1
   
   print("lower = ",l)
   print("upper = ",u)


str=input("Enter a string ")
countAlp(str)
