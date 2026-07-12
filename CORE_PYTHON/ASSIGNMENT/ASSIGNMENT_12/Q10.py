# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

def largeStr(string1,string2):
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
        print('both strings have same lenght.')        
    
string1 = input('Enter string 1 : ')
string2 = input('Enter string 2 : ')

res = largeStr(string1,string2)

print('larger string is : ',res)