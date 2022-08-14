a=int(input("Enter a number"))
count=0;
if a>1:
  for c in range(2,a):
    if(a%c == 0):
      print("Not prime number")  
      break  
  
  else: 
    print("prime number")    
else:
 print("Not prime number")  