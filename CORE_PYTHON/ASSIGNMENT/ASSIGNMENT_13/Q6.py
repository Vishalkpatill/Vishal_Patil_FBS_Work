# Python Program to Multiply All the Items in a Dictionary

from math import prod

def productValue(dict):
    
    return (prod(dict.values()))

dict = {'a' : 1, 'b' : 2, 'c' : 3}

res = productValue(dict)

print('Product of values is :',res)