
class Employee:
    global l
    l=[]
    def __init__(self,Empno,ename,sal):
        self.Empno=Empno
        self.ename=ename
        self.sal=sal
    def create_New_Emp(self):
        print("Employee detailes only")
    def Delete_Emp(self):
        pass
    def display_emp():
        print([e1.Empno,e1.ename,e1.sal])
class job:
    def __init__(self,job,losal,hisal):
        self.job=job
        self.losal=losal
        self.hisal=hisal
class new(Employee,job):
    def create_New_Emp():
        print("New Employee had been created")
    def display_emp():
        print([e1.Empno,e1.ename,e1.sal,e2.job,e2.losal,e2.hisal])
e1=Employee(1,"rajesh",24000)
e2=job("manager",10000,25000)
new.create_New_Emp()
new.display_emp()

