# Duck object method
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
        print("Cricle")
        self.area=math.pi*self.radius

    def display_area(self):
        print(self.area)

class Square:
    def __init__(self,side):
        self.side=side
        self.area=self.side**2

    def display_area(self):
        print(self.area)

C1=Circle(10)
C1.display_area()
S1=Square(25)
S1.display_area()

# polymorphism by using built in fuction
L1=[12,25,15,2056]
S1="ALi"
print(len(L1),type(L1))
print(len(S1),type(S1))    
