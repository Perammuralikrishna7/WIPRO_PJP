Str=input("Enteer the string:")
l=len(Str)
nxt=" "
if(l<=1):
    nxt=Str
else:
    for i in range(0,l):
        nxt=nxt+Str[0]+Str[1]
print(nxt)