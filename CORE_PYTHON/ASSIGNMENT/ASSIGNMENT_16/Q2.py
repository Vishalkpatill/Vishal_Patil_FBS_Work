# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowProduct
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product():
    discount = 10

    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def applyDiscount(self):
        amount = (self.price * Product.discount) / 100
        self.price = self.price - self.discount
        print(f'Discount of {Product.discount}% is applied')


    def showProduct(self):
        print(f'pid: {self.pid}\tpname: {self.pname}\tprice: {self.price}\tquantity: {self.quantity}')

    
    def __del__(self):
        print('Product object has destroyed')


p1 = Product(101, 'facewash', 300, 1)
p1.showProduct()

p1.applyDiscount()
p1.showProduct()
