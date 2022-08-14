def addition(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


list1 = [8,2,3,0,7]
i = addition(list1)
print(i)