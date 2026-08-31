# Python Program to Add a Key-Value Pair to the Dictionary

def addKeyValue(dict, key, value):
    dict[key] = value
    return dict

newDict = {}

addKeyValue(newDict, 'name', 'Vishal')
addKeyValue(newDict, 'age', 23)

print(newDict)
