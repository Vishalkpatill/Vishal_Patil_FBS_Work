# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook


class Book():

    def __init__(self, bid= 0, bname= '', price = 0, author = ''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print('Book object is destroyed')    

    def ShowBook(self):
        print(f'bid : {self.bid}\tbname : {self.bname}\tprice : {self.price}\tauthor : {self.author}')

b1 = Book()
b1.ShowBook()

b2 = Book(101, 'class programming', 650, 'vishalpatil')
b2.ShowBook()