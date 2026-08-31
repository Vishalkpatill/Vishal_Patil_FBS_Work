# Python Program to Check if a Given Key Exists in a Dictionary or Not

def keyExist(dict,key):
    if key in dict:
        return 'key exist'
    else:
        return 'key not exist'
    
stu = {'name' : 'vishal', 'age' : 23, 'city' : 'Nashik'}

key = input('Enter key : ')

res = keyExist(stu,key)

print(res)