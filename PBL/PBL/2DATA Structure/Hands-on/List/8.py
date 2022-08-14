i=5
a=[]
while i>0:
    num=int(input("Enter number: "))
    a.append(num)
    i=i-1
index=int(input("Enter the specified number1"))
a.remove(index)
print("Final list",a)