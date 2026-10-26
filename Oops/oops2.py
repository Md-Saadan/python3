class School:
    # instant class
    School_Name="ATT Heigh School And Junior College"
    def __init__(self,student_name,marks):
        # instant variable
        self.student_name=student_name
        self.marks=marks
    
    def display(self):
        print(self.student_name,self.marks)

    # instant method
    @classmethod
    def display_info(cls,a):
        cls.a=a
        print("This is Basic info")
        print(cls.a)
   

S1=School("Aman",450)
S2=School("Ali",500)
S1.display()
S2.display()

School.School_Name="MHS"
print(School.School_Name)

School.display_info(76)


