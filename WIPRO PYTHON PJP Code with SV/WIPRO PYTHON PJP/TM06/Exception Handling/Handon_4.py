b=[1,2,3,4,5,-6,-9,10,22,60]

try:
   a=int(input("Enter the index to find "))
   if b[a]>0:
      print("Positive Number")
   elif b[a]<0:
      print("Negative Number")

except IndexError:
   print("Not a valid index")