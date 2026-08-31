# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book():

    count = 0

    def __init__(self, bid=0, bname='', price=0, author=''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def __del__(self):
        print('Book object is destroyed.')

    def ShowBook(self):
        print(f'bid :{self.bid}\tbname :{self.bname}\tprice :{self.price}\tauthor :{self.author}')

b1 = Book(101, 'sapiens', 299, 'xyz')
b2 = Book(102, 'ikagai', 399, 'yxz')
b3 = Book()

b1.ShowBook()
b2.ShowBook()
b3.ShowBook()

print('total object :', Book.count)

