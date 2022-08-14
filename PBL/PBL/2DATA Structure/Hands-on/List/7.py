i=5
a=[]

while i>0:
    num=int(input("Enter number: "))
    a.append(num)
    i=i-1
index=int(input("Enter the specified index"))
a.pop(index)
print("Final list",a)