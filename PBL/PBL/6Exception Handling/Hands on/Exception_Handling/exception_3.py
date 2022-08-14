try:
    n = input("Enter the file name : ")
    file = open(n, "r")
    f1 = file.read()
    print(f1.title())      
    file.close()

except:
    print("File Not Found Error occured")