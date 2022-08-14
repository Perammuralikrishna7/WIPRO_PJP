a=[2,3,6,6,5]

m=a[0]
m1=a[0]

n=len(a)

for i in range(0,n):
   if a[i]>m:
       m1=m
       m=a[i]
   elif a[i]>m1 and m!=a[i]:
       m1=a[i]
   else:
       if m1==m:
          m1=a[i]


print(m1)
   