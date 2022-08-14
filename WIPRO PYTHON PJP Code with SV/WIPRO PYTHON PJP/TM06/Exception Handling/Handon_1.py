a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))

try:
   c=a//b
except ZeroDivisionError:
   print("Divide by zero error")
else:
   print("Result ",c)