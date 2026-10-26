# Multilevel inheritance:
class Products:
    def __init__(self,pid):
        self.pid=pid
        print("Products")

class Categery(Products):
    def __init__(self,pid,pcategry,pname,price):
        super().__init__(pid)
        self.pcategry=pcategry
        self.pname=pname
        self.price=price
        print("Categry")

class Order(Categery):
    def __init__(self, pid, pcategry, pname, price,qty,payment_method):
        super().__init__(pid, pcategry, pname, price)
        self.qty=qty
        self.payment_method=payment_method
        print("Order")

    def amount(self):
        print("Order Details")
        print(self.pid,self.pcategry,self.pname, self.price,self.qty,self.payment_method)
        return self.qty*self.price
    
O1=Order("101","Spoarts","Cycle","15000","3","COD")
O2=Order("102","Spoarts","Bike","115000","1","UPI")
O3=Order("103","Computer","Laptop","90000","2","credit Cart")

orders=[O1,O2,O3]
total_amount=0
print("Total Bill Amount")
for O in orders:
    total_amount+=O.amount()
print("total bill amount=",total_amount)
    