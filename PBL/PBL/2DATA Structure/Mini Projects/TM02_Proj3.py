dict={"Krishna":[67,68,69],"Arjun":[70,98,63],"Malika":[52,56,60]}
x=input("Enter a name:")
for i in list(dict.keys()):
    if(x==i):
        print("Average percentage mark:",sum(dict[i])/len(dict[i]))
        



