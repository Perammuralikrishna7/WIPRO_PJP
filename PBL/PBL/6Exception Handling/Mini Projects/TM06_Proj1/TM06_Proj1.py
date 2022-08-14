try:
    f = input("Enter the file name : ")
    file = open(f,"r")
    d={}            # dictionary

    for i in file:
        if i != "\n":
            (key,val) = i.strip().split(" ")
            d[key] = val
        
    print(d,"\n")
    
    total = 0 
    dis = 0
    ctr = 0
    free_count = 0

    for i in d.keys():          # To count the no of items
        if i != "Discount":
            ctr = ctr+1

    for i in d.values():        # To count the Free items
        if i == "Free":
            free_count = free_count+1

    print("No of items purchased: ",ctr-free_count)
    print("No of free items: ",free_count)

    for i,j in d.items():       # Amount to pay
        if j != "Free":
            if i != "Discount":     
                total = total + int(j)

    print("Amount to pay: ",total)

    for i,j in d.items():       # Discount amount
        if i == "Discount":
            dis = j

    dis = int(dis)
    total = int(total)

    if (dis < total):
        print("Discount given: ",dis)
        print("Final amount paid: ",total-dis)
    else:
        raise ValueError()
        
    file.close()
    
except FileNotFoundError:
    print("File not found error occured")
    
except ValueError:
    print("Discount should be less than the total amount to be paid")