# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowProduct

class Product():

    def __init__(self, pid=0, pname='', price=0, quantity=0):

        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print('Product object is destroyed')

    def ShowProduct(self):
        print(f'pid :{self.pid}\tpname :{self.pname}\tprice :{self.price}\tquantity :{self.quantity}')

# p1 = Product()
# p1.ShowProduct()

p2 = Product(1, 'Phone', 25000, 5)
p2.ShowProduct()
