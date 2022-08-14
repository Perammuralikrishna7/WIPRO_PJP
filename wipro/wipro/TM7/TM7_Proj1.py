#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle

def set_data():
    ID=int(input("Enter Employee ID:"))
    name=input("Enter Employee Name:")
    age=int(input("Enter Employee Age:"))
    salary=float(input("Enter Employee Salary:"))
        
    #creating a list
    Employee=[ID,name,age,salary]
        
    return Employee

def display(Employee):
    print(Employee[0],Employee[1],Employee[2],Employee[3])
    print()
    
def write_record():
    #open file in binary mode for writing
    outfile=open('emp.dat','ab')
    
    #serilialize the object and writing to file
    pickle.dump(set_data(),outfile)
    
    #close the file
    outfile.close()

def read_records():
    #open file in binary mode for reading
    infile=open('emp.dat','rb')
    
    # read to the end of file.
    while True:
        try:
            #reading the object from file
            Employee=pickle.load(infile)
            
            #display the object
            display(Employee)
        except EOFError:
            break
    
    #close the file
    infile.close()
    
def show_choice():
    print("Main Menu")
    print("1.Add an Employee")
    print("2.Display All")
    print("3.Exit")
    
def main():
    while(True):
        show_choice()
        choice=int(input("Enter choice(1-3):"))
        
        print()
        
        if choice==1:
            write_record()
        
        elif choice==2:
            read_records()
            
        elif choice==3:
            break
            
        else:
            print("Invalid input")
    
main()

