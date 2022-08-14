def case(s):
    lower=0
    upper=0
    for c in s:
        if (c >= 'a') and (c <= 'z'):
            lower += 1
        elif (c >= 'A') and (c <= 'Z'):
            upper += 1

    lis = [lower,upper]
    return lis


s = input("Enter a string: ")
list1 = case(s)

print("Lower case letters: ",list1[0])
print("Upper case letters: ",list1[1])