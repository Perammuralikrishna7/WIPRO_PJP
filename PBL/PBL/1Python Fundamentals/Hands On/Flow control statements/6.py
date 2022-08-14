n=int(input("Enter a number="))
m=n//2
flag=0
for i in range(2,m):
    if((m%i) == 0):
        flag=1
        break
if(flag==0):
    print("It is a prime number")
else:
    print("It is not a print number")