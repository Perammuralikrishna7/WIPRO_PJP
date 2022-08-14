print("Enter the 2 numbers ")
n1 = int(input())
n2 = int(input())

try:
    print( n1,"divided by",n2,"is", n1//n2 )
except ZeroDivisionError:
    print("No number can be divided by Zero ")
