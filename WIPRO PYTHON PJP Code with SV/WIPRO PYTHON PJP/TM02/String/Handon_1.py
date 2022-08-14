a="Welcome to Wipro Technologies"
u=0
l=0
print(a)

for i in a:
   if (i.isupper()):
     u=u+1
   elif (i.islower()):
     l=l+1


print("lower = ",l)
print("upper = ",u)