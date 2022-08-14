from sys import argv

a=argv[1]
b=argv[2]
c=argv[3]

ali=a.split('-')
bli=b.split('-')
cli=c.split('-')

c=0

al=len(ali)
bl=len(bli)


for i in range(0,al,1):
   if ali[i] in cli:
      c=c+1

for j in range(0,bl,1):
   if bli[j] in cli:
       c=c-1

print(c)



