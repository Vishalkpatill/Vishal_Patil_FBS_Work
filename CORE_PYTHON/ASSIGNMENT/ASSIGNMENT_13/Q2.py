def concatDict(dict1, dict2):
    dict1.update(dict2)
    return dict1

dict1 = {'name' : 'Vishal' , 'age' : 23}

dict2 = {'height' : 5.8,'weight' : 63}

res = concatDict(dict1, dict2)

print(res)