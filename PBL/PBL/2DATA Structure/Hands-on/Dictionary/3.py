key=int(input("Enter the key to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)
n=int(input("Enter a key to check"))
if n in d:
    print("present")
else:
    print("Not present")