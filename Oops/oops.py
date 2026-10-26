class student:
     def __init__(self,name,roll_no,marks):
          self.name=name
          self.roll_no=roll_no
          self.marks=marks
          print("This is called as Construtctor")

     def display_data(self):
      print(self.name)
      print(self.roll_no)
      print(sum(self.marks))
      print(sum(self.marks)/len(self.marks))

s1=student("Hadi","2",[25,25,56,46])
s2=student("Sameed","3",[25,62,25,50])
s1.display_data()
s2.display_data()


     
     
          