f1=open('sample1.txt','r')

str=f1.read()
li=str.split(' ')
m=" "
for i in li:
    if len(i)>len(m):
        m=i


print(m)
f1.close()
      


