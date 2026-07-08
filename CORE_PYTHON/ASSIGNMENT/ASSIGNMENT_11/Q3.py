# Python Program to Sort the List According to the Second Element in Sublist

def sort_list(li):    

    li.sort(key = lambda x : x[1]) ## 
    return li

li = [['Vishal',19],['Gaurav',11],['Ketan',6],['Prakash',20]]

print('random list :\n',li)


res = sort_list(li)

print('sorted list accd to 2nd ele :\n',res)