st=input("Enter the string:")
a=" "
n=int(input("Enter a number:"))
l=len(st)

for i in range(0,n):
    a=a+st[l-n:]
print(a)