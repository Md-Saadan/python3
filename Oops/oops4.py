# Multiple Inheritance
class Personal:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        print("Personal")

class Acadimics:
    def __init__(self,education,marks):
        self.education=education
        self.marks=marks
    def calculate_percentage(self):
     return (sum(self.marks) / (len(self.marks) * 500)) * 100

def calculate_grade(self):
    if self.percent >= 90:
        return "A+"
    elif self.percent >= 80:
        return "A"
    elif self.percent >= 70:
        return "B+"
    elif self.percent >= 60:
        return "B"
    elif self.percent >= 50:
        return "C"
    else:
        return "D"

class Skill:
    def __init__(self,skillset):
        self.skillset=skillset
        print("Skill")

class Employee(Personal,Acadimics,Skill):
    def __init__(self, name, gender,education,marks,grade,skillset,emp_id,companey,salary):
        Personal.__init__(self,name,gender)
        Acadimics.__init__(self,education,marks,grade)
        Skill.__init__(self,skillset)
        self.emp_id=emp_id
        self.companey=companey
        self.salary=salary

    def display_data(self):
        print(self.name,self.gender,self.education,self.marks,self.grade,self.skillset,self.emp_id,self.companey,sep="\n")

    
E1=Employee("Ali","Male","BCA",450,"B+",["c","c++","python"],101,"XYZ",25000)
E1.display_data()



        

