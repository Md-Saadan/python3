import time
import threading

'''
def f1(a,b,c):
    print("This is Square")
    print(f"{a}  {b}  {c}")

t1=threading.Thread(target=f1,args=("Data","Tables","Colours"))
t1.start()
'''
sq=[]
cb=[]

def Square(s,e,a,Name,version):
    for i in range(s,e):
        # print(a,time.strftime("%H:%M:%S --"),":",i*i)
        print(a,time.ctime(),":",i*i,Name,version)
        sq.append(i*i)
        time.sleep(2)

def Cube(s,e,b,Name,version,Year):
    for i in range (s,e):
        # print(b,time.strftime("%H:%M:%S --"),":" , i*i*i)
        print(b,time.ctime(),":",i*i*i)
        print(Name,version,Year)
        cb.append(i*i*i)
        time.sleep(2)

t1=threading.Thread(target=Square,args=(1,2,"Square"),kwargs={"Name":"thread","version":1.1})
t2=threading.Thread(target=Cube,args=(1,2,"cubes"),kwargs={"Name":"thread","version":1.2,"Year":25})

t1.start()
t2.start()

t1.join()
t2.join()
