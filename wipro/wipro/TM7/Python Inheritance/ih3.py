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
class Contract_Employees:
    def __init__(self,Empno,ename,sal,contract_start,contract_end):
        self.Empno=Empno
        self.ename=ename
        self.sal=sal
        self.contract_start=contract_start
        self.contract_end=contract_end
    def create_New_Emp(self):
        print("contract Employee detailes only")
    def Delete_Emp(self):
        pass
    def display_emp(self):
        print(self.__dict__)
c=Contract_Employees(120,"Ravi",10000,"25-04-2022","25-05-2022")
c.create_New_Emp()
c.display_emp()