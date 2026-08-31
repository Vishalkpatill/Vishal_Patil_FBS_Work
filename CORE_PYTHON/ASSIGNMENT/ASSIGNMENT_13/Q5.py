# Python Program to Sum All the Items in a Dictionary

def sumAll(dict):
    
    return f'sum :', sum(dict.values())


dict = {'math': 100, 'physics' : 90, 'english' : 70}

res = sumAll(dict)
print(res)