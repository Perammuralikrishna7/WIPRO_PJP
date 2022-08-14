class Employee:
    global l
    l=[]
    def __init__(self,Empno,ename,sal):
        self.Empno=Empno
        self.ename=ename
        self.sal=sal
    def create_New_Emp(self):
        print("[Empno->",self.Empno,"ename->",self.ename,"sal->",self.sal,"]")
        l.append([self.Empno,self.ename,self.sal])
    def Delete_Emp(self):
        pass
    def display_emp():
        if l[0][2]>l[1][2] and l[0][2]>l[2][2]:
            print(l[0])
        elif l[1][2]>l[0][2] and l[1][2]>l[2][2]:
            print(l[1])
        else:
            print(l[2])
e1=Employee(1,"rajesh",266000)
e1.create_New_Emp()
e2=Employee(2,"Rahul",25200)
e2.create_New_Emp()
e3=Employee(3,"Rebal",25400)
e3.create_New_Emp()
Employee.display_emp()

