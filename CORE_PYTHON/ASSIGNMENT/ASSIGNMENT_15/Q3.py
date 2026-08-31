# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowShirt

class Shirt():
    def __init__(self, sid=0, name= '', type='',price=0, size=''):
        self.sid = sid
        self.name = name 
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print('Shirt object is destroyed.')

    def ShowShirt(self):
        print(f'sid :{self.sid}\tname :{self.name}\ttype :{self.type}\tprice :{self.price}\tsize :{self.size}')

s1 = Shirt()
s1.ShowShirt()

s2 = Shirt(19, 'Vishal', 'Casual', 699, 'M')
s2.ShowShirt()
