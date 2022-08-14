def fact(a):
    f=1
    for i in range(1,a+1,1):
       f=f*i
    return f


x=int(input("Enter a number "))
fac=0
if(x>0):
    fac=fact(x)
    print(fac)

else:
    print("Enter a valid number")
