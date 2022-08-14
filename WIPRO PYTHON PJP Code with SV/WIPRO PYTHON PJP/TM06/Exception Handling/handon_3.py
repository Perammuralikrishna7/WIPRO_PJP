try:
   fileName=input('Enter the file name to open ')   
   f=fileName+'.txt'
   f1=open(f,'r')

except FileNotFoundError:
   print("File does not exist")
else:
   print(f1.read())
   