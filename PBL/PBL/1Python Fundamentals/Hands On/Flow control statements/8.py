n=int(input("Enter number"))
s=0
while(n!=0):
    last_digit=n%10
    s=s+last_digit
    n=n//10
print(s)