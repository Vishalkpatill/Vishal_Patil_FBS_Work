# Python Program to Remove the Given Key from a Dictionary

def removeKey(dict):
    
    return dict.pop('city')

dict = {'name' : 'Vishal', 'age' : 23, 'city' : 'Pune'}

res = removeKey(dict)

print(dict)