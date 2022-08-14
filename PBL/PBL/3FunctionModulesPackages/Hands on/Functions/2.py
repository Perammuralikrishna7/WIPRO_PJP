def reverse(s):
    str1 = ""
    for i in s:
        str1 = i + str1
    return str1


str2 = input("Enter a String: ")
print("The original string is: ", str2)
print("The reverse string is", reverse(str2))
