from classes.order import Order

class Coffee:
    def __init__(self, name:str):
        self._name = name 
        self._orders = []

    def getname(self):
        return self._name
    
    def setname(self, name):
        name

    def addOrder(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders
    
    def customers(self):
       # customerList = []
       # for order in self.orders():
       #    if order.customer not in customerList:
       #         customerList.append(order.customer)
       # return customerList
         return list(set(map(lambda order: order.customer, self.orders())))
    

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total_price = 0
        for order in self.orders():
            total_price += order.price
        return total_price / len(self.orders())



    name = property(getname, setname)

