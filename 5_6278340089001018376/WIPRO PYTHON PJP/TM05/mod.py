def countWord(a):
   f1=open(a,'r')
   b=f1.read()
   c=dict()
   w=b.split()
   
   for wo in w:
       if wo in c:
           c[wo] +=1
       else:
           c[wo] = 1

   m=0
   p=" "
   for i in c:
      if c[i]>m:
         m=c[i]
         p=i   
   
   f1.close()
   return p


def findTime(a):
   f1=open(a,'r')
   li=f1.readlines()
   l=len(li)
   return l