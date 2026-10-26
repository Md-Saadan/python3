# OPerator overloading
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            print("The Points Are Same")
        else:
            print("Points Are Not Same")
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

P1=Point(10,20)
P2=Point(30,40)
P1==P2

