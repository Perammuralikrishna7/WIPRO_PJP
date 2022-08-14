Str=input("Enter the string:")
l=len(Str)

if(Str[0]=='x'):
    Str=Str[1:l]
    l=len(Str)
    
if(Str[l-1]=='x'):
    Str=Str[0:l-1]
print(Str)