class Person:
    def __init__(self,name,age,gender):
     self.name=name
     self.age=age
     self.gender=gender
     print("This is called Parent Class Constructor")

    # def display(self):
    #     print("Name:",self.name)
    #     print("Age:",self.age)
    #     print("Gender:",self.gender)


class Student(Person):
    def __init__(self,name,age,gender,roll,marks,school):
        super().__init__(name, age, gender)
        self.roll=roll
        self.marks=marks
        self.school=school
        print("This Is Called As Child Constructor")

    def display_data(self):
        print("Roll Number:",self.roll)
        print("Marks:",self.marks)
        print("School Name:",self.school)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

S1=Student("Ali",15,"Male",101,550,"ATT")
S1.display_data()

    