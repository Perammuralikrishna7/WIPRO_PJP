def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n%x == 0:
                return False
            else:
                return True


i = int(input("Enter a number"))
print(is_prime(i))