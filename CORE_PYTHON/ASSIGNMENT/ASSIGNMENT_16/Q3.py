# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowShirt
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class shirt():
    pIncrease = 10

    def __init__(self, sid=0, sname='', type='', price=0, size='small'):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def increasePrice(self):
        if self.size == 'medium':
            self.price = self.price + (self.price * shirt.pIncrease / 100)
        elif self.size == 'large':
            self.price = self.price + (self.price * 2 * shirt.pIncrease / 100)
        elif self.size == 'xlarge':
            self.price = self.price + (self.price * 3 * shirt.pIncrease / 100)

    def ShowShirt(self):
        print(f'sid: {self.sid}\tsname: {self.sname}\ttype:{self.type}\tprice: {self.price}\tsize: {self.size}')

    def __del__(self):
        print('Shirt object destroyed.')

s1 = shirt(19, 'V19', 'casual', 3000, 'large')

print('price before updation')
s1.ShowShirt()

s1.increasePrice()
print('Price after updation')
s1.ShowShirt()