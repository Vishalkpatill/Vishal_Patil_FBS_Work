# 15. Python Program to find larger string without using built-in functions.

def lagersString(string1,string2):

    count1 = 0
    count2 = 0

    for i in string1:
        count1 = count1 + 1

    for i in string2:
        count2 = count2 + 1

    if count1 > count2:
        return string1

    elif count2 > count1:
        return string2

    else:
        print('both string have same length')

string1 = input('enter 1st string :') 
string2 = input('Enter 2nd string :')

res = lagersString(string1,string2)

print('larger string is',res)