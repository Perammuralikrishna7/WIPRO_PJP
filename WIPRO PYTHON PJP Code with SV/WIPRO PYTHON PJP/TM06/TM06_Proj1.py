fileName=input("Enter the you want to open with extension ")
try:
   f1=open(fileName,'r')
except FileNotFoundError:
   print("Not a valid file")
else:
   dis=0
   itemCount=0
   freeItem=0
   sum=0
   totalAmount=0
   while(True):
      line=f1.readline()
      if not line:
         break
      if not line.isspace():
         item=line.split()         
         if item[0]=='Discount':
            dis=int(item[1])         
         else:
            itemCount +=1
            if item[1]=='0':
               freeItem +=1    
            sum +=float(item[1])
         
   totalAmount=sum-dis
   print("No. of item Purchased:",itemCount)
   print("No. of free items:",freeItem)
   print("Amount to pay:",sum)
   print("Discount Given:",dis)
   print("Final amount paid:",totalAmount)
        
   
   
