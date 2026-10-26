#1
class Person:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("Person")

class Sports(Person):
    def __init__(self, name, city,sport):
        super().__init__(name, city)
        self.spoart=sport
        print("Sport")

    def display_data(self):
        print(self.name,self.city,self.spoart)

class Skill(Person):
    def __init__(self,name,city,skill_set):
        super().__init__(name,city)
        self.skill_set=skill_set
        print("Skill")

class Academics(Person):
    def __init__(self,name,city,education,grade):
        super().__init__(name,city)
        self.education=education
        self.grade=grade
        print("Acadimics")
class Employee(Academics,Skill):
    def __init__(self, name, city, education, grade,skill_set,company,designation):
        super().__init__(name, city, education, grade,skill_set)
        self.company=company
        self.designation=designation
        print("Employee")

    def display(self):
        print(self.name,self.city)
        print(self.education,self.grade)
        print(self.skill_set,self.company)
        print(self.designation)

S1=Sports("Ali","Malegaon","Football")
S1.display_data()
E1=Employee("Ahmad","Nashik",["python","C","C++"],"Microsoft","Developer")
E1.display()

# 2
class Personal:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print("Personal")


class Acadimics:
    def __init__(self, education, marks):
        self.education = education
        self.marks = marks
        self.percent = self.calculate_percentage()
        self.grade = self.calculate_grade()
        print("Academics")

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
    def __init__(self, skillset):
        self.skillset = skillset
        print("Skill")


class Employee(Personal, Acadimics, Skill):
    def __init__(self, name, gender, education, marks,
                 skillset, emp_id, company, salary):

        Personal.__init__(self, name, gender)
        Acadimics.__init__(self, education, marks)
        Skill.__init__(self, skillset)

        self.emp_id = emp_id
        self.company = company
        self.salary = salary

    def display_data(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Education:", self.education)
        print("Marks:", self.marks)
        print("Percentage:", round(self.percent, 2), "%")
        print("Grade:", self.grade)
        print("Skills:", self.skillset)
        print("Employee ID:", self.emp_id)
        print("Company:", self.company)
        print("Salary:", self.salary)


E1 = Employee(
    "Ali",
    "Male",
    "BCA",
    [450, 400, 350],
    ["C", "C++", "Python"],
    101,
    "XYZ",
    25000
)

E1.display_data()
    

