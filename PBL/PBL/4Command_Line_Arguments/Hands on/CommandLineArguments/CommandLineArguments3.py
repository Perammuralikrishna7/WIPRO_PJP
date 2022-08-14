from sys import argv
S = 0
def isprime(n):
    if (n<=1):
        return False
    else:
        for i in range(2,int(n/2)+1):
            if(n%i == 0):
                return False
            elif(i == int(n/2)):
                return True
S = 0
for i in argv[1:]:
    if(isprime(int(i))):
        S += int(i)
print(S)