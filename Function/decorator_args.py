'''def admission(func):
    def wrapper(*args,**kwargs):
        print("This is Pune University")
        print(f"This has {len(args)} args")
        print(f"This has {len(kwargs)} Keywoard Argument")
        func(*args,**kwargs)
        print("Thank you!")
    return wrapper

@admission
def FE_admission(sname,marks):
    print(f"The Student Name:{sname}")
    print(f"This is Total CET marks={sum(marks)}")
FE_admission("Saadan",[70,80,90])

@admission
def BSC_admission(a_id,a_name,a_marks,categrey):
    print(f"Candidate id:{a_id}")
    print(f"Candidate name:{a_name}")
    print(f"Candidate marks:{a_marks}")
    print(f"Candidate categry:{categrey}")
    print(f"Total marks:{sum(a_marks)}")
BSC_admission(5454568,"Sahil",a_marks=[25,52,58,25],categrey="OBC")'''

def odd_even(func):
    def wrapper(num):
        #  num=print(int(input("Enter the Number ")))
           
        if num%2==0:
            print("The Number is Even")
            func(num)
        else:
            print("The Number is Odd")
    return wrapper


@odd_even
def display(num):
    print("The Number is",num)
display(10)
display(5)


