import time
import threading

def Display():
    l1=[1,2,3,4,5,6,7,8,9,10]
    for i in l1:
        print("Display",i)
        time.sleep(2)

def Sum():
    l1=[11,22,33,44,55,66,77,88,99]
    s=0
    for i in l1:
        s+=i
        print("Sum",s)
        time.sleep(2)

def Stringf():
    S1="Python"
    l1=[]
    for i in S1:
        l1.append(i)
        print(l1)
        time.sleep(2)

t1=threading.Thread(target=Display)
t2=threading.Thread(target=Sum)
t3=threading.Thread(target=Stringf)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


