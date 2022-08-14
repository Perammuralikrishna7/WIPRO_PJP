
try:
   a=int(input("Enter a number to check prime "))


except ValueError:
   print("Enter a valid number")

else:
   c=0
   for i in range(2,a,1):
      if a % i == 0: 
         c=c+1

   if c==0:
      print("Prime Number")
   else:
      print("Not a prime Number")
  
