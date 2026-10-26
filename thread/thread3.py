# import time 
# import threading
# import os

# def file_read_write(file1,file2):
#     os.chdir("D:\\Saadan")
#     print(os.getcwd())

#     mydata=" "
#     with open(file1,"r") as f1:
#         mydata=f1.read()
#         print(mydata)
#         f1.close()
#         print(time.ctime())

#     os.chdir("D:\\Saadan\\ECOMMERCE")
#     with open (file2,"w") as f2:
#         f2.write(mydata)
#         f2.close()
# # file_read_write()
# t1=threading.Thread(target=file_read_write,args=("contents.txt","New_contents.txt"))
# t1.start()
# t1.join()

import time 
import os
os.chdir("D:\\Saadan")
with open("")