class Employee:
    def __init__(self,empid,ename,companey):
        self.empid=empid
        self.ename=ename
        self.companey=companey

    def display(self):
        self.display
        print("Employee id:",self.empid)
        print("Employee Name:",self.ename)
        print("Employee Companey:",self.companey)

class Sales(Employee):
    def __init__(self, empid, ename, companey,profile,team):
        super().__init__(empid, ename, companey) 
        self.profile=profile
        self.team=team

    def display_sales(self):
        self.display()
        print(self.profile,self.team,sep="\n")
        
class HR(Employee):
    def __init__(self, empid, ename, companey,management_level):
        super().__init__(empid, ename, companey)
        self.management_level=management_level

    def display_HR(self):
        self.display()
        print(self.management_level,sep="\n")

class Development(Employee):
    def __init__(self, empid, ename, companey,skills,project):
        super().__init__(empid, ename, companey)
        self.skills=skills
        self.project=project

    def display_Dev(self):
        self.display()
        print(self.skills,self.project,sep="\n")

S1=Sales(101,"WAseem","TCS","Junior Sales man","Beta")        
H1=HR(102,"Ahmed","Infosys","HR Maneger")
D1=Development(103,"Saadan","ABC",["python","C","java"],"XYZ")

S1.display()
H1.display_HR()
D1.display_Dev()
