try:
    n1 = int(input("Enter a number : "))
    flag = 0

    if n1 == 1:
        print("1 is neither Prime nor Composite ")
    else:
        for i in range(2, (n1//2)+1 ):
            if n1%i == 0:
                flag = 1
                break
            
    if flag == 1:
        print("NOT a prime")
    else:
        print("PRIME")

except ValueError:
    print("Value Error occured !!! Enter a valid number ")