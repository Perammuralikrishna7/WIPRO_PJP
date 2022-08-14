a=[1,2,3,4,5]
b=[11,21,22,23,25]

print("List 1")
for i in a:
  print(i)

print("List 2")
for j in b:
  print(j)

a.extend(b)

print("List after append")
for k in a:
  print(k)


