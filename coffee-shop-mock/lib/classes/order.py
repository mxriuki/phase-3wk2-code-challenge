
class Order:
    all = []


    def __init__(self, customer, coffee, price):
         self.customer = customer
         self.coffee = coffee
         self.price = price 


         coffee.addOrder(self)
         customer.addOrder(self)
         Order.all.append(self)


    
   
