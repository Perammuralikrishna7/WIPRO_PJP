a=input("Enter a string to check palindrome ")
p=""

for i in a:
   p=i+p
   if(a==p):
      print("Palindrome")
      break
else:
   print("Not palindrome")      