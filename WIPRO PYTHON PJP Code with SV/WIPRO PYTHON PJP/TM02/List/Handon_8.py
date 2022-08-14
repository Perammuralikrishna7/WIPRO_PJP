a=[1,2,3,4,5,23,45,1,2,3,5,5]

for i in a:
  print(i)

b=int(input("Enter the number of which 1 occurance to remove"))
c=0
for i in a:
  if i==b:
     break
  c=c+1 


del a[c]
print ("list after removal of specified number ")
i=0
for i in a:
  print(i)