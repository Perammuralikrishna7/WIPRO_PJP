i=5
a=[]
count=0
while i>0:
    num=int(input("Enter number: "))
    a.append(num)
    i=i-1
i=int(input("Enter a number to be evaluated: "))

print("No of occurences is",a.count(i))