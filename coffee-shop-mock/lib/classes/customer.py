from classes.order import Order

class Customer:
    def __init__(self, name):
        self._name = name 
        self._orders = []

    def getname(self):
        return self._name 

    def setname(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
             self._name = name 

    def addOrder(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(map(lambda order: order.coffee, self.orders())))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)




    name = property(getname, setname)

