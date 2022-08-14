i=5
a=[]
while i>0:
    num=int(input("Enter number: "))
    a.append(num)
    i=i-1

a.reverse()
print("Reverse Order is",a)