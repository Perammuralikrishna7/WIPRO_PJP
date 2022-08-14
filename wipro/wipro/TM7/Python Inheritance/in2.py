class Employee:
    def __init__(self,Empno,ename,sal):
        self.Empno=Empno
        self.ename=ename
        self.sal=sal
    def create_New_Emp(self):
        print("Employee detailes only")
    def Delete_Emp(self):
        pass
    def display_emp(self):
        print(self.__dict__)
class EmployeeBonus(Employee):
    def __init__(self,Empno,ename,sal,bonus):
        self.Empno=Empno
        self.ename=ename
        self.sal=sal
        self.bonus=bonus
    def create_New_Emp(self):
        print("Employee detailes with bonus")
    def Delete_Emp(self):
        pass
    def display_emp(self):
        print(self.__dict__)
e1=EmployeeBonus(1,"gopi",25000,10000)
e1.create_New_Emp()
e1.display_emp()