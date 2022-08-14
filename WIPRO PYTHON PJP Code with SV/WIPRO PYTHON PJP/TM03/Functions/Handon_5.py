def printEven(li):
  lieven=[]
  for i in li:
     if i%2==0:
       lieven.append(i)
  
  return lieven


li=[1,2,3,4,5,6,7,8,9]
print(printEven(li))