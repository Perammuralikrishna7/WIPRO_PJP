def checkPrime(a):
   c=0
   for i in range(2,a,1):
      if a % i == 0: 
         c=c+1

   if c==0:
      print("Prime Number")
   else:
      print("Not a prime Number")




a=int(input("Enter a number: "))
checkPrime(a)