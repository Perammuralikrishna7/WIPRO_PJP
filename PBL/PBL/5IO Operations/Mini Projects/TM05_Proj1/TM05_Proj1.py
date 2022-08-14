file = open("sample.txt", "r")
f1 = file.read()
s = f1.split("\n")
ctr = 0

for i in s:
    if i:
        ctr = ctr+1

if ctr >=1 and ctr <=12:        # Meeting time
    print("Meeting Time : ",ctr,"AM")

if ctr >12 and ctr <= 24:   
    if ctr == 24:
        ctr = ctr-12
        print("Meeting Time : ",ctr,"AM") 
    else:
        ctr = ctr-12
        print("Meeting Time : ",ctr,"PM")
        
file.close()


file = open("sample.txt", "r")    # Meeting place
nlist = []

for i in file:   
    for j in i.split():       
        nlist.append(j) 

maximum = nlist.count(nlist[0])

for i in nlist:
    len1 = nlist.count(i)
    
    if len1 > maximum:
        maximum = len1
        ind = nlist.index(i)
        
print("Meeting Place : ",nlist[ind],"Street")

file.close()