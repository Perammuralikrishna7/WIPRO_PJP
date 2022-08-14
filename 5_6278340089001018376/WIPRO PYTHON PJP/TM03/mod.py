def ispalindrome(name):
  str=""
  for i in name:
      str=i+str
  
  if name == str:
       print("Yes it is a palindrome")
  else:
       print("No it is not palindrome")



def count_the_vowels(name):
   a=name.count('a')
   A=name.count('A')
   e=name.count('e')
   E=name.count('E')
   i=name.count('i')
   I=name.count('I')
   o=name.count('o')
   O=name.count('O')
   u=name.count('u')
   U=name.count('U')
   sum=a+e+i+o+u+A+E+I+O+U
   print("No of vowels are: ",sum)



def frequency_of_letters(name):
   f={}
   for char in name:
      if char in f:
         f[char] +=1
      else:
         f[char] = 1
   
   print ("frequency of letters :")
   for k in f:
     if k!=" ":
        print(k,"-",f[k],end=" ")   
    
