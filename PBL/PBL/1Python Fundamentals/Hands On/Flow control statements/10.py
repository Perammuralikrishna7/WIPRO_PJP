num=int(input("Enter a number="))
number=num
rev=0
while(num!=0):
    remainder=num%10
    rev=rev*10+remainder
    num=num//10
if(number==rev):
    print("It is a palindrome")
else:
    print("It is not a palindrome")