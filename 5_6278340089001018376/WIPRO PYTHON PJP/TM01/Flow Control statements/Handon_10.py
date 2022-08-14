a=int(input("Enter a number"))

b=a

sum=0

while(a>0):
  ld=a%10
  sum=(sum*10)+ld
  a=a//10

if(b==sum):
  print(b," is a palindrome")
else:
  print(b," is not a palindrome")

 