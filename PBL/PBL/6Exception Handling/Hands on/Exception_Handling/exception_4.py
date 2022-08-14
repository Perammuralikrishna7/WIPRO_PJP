nlist = []
print("Enter 10 integers : ")
for i in range(0,10):
    val = int(input())
    nlist.append(val)
    
print(nlist)

ind = int(input("Enter the index : "))

try:  
    val = nlist[ind]
    if val > 0:
        print(val,"is a Positive Integer")
    if val < 0:
        print(val,"is a Negative Integer")

except:
    print("Index Error occured")
