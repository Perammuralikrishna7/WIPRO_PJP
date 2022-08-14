from sys import argv

def checkPrime(a):
   c=0
   for i in range(2,a,1):
      if a % i == 0: 
         c=c+1

   if c==0:
      return 1;
   else:
      return 0;

total = 0   # to collect the prime numbers
count = 1   # a counter for the numbers that you entered
for i in range(1,11,1):
   num = int(argv[i])
   if num > 1:  # if number is larger than 1, we need to check
      if checkPrime(num)==1:
          total+=num
   elif num == 1:   # 1 is a prime number
      total += num
   else:   # otherwise the number is negative so we skip.
      pass
   count += 1
print("\nTotal : {}".format(total))