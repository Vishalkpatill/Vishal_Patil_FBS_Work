# Python Program to Find the Union of two Lists

def union(li1,li2):
    uni = list(set(li1).union(set(li2)))
    return uni

li1 = [1, 2, 3, 4]
li2 = [5, 2, 7, 4, 9, 10]
print('list 1 :',li1)
print('list 2 :',li2)


res = union(li1,li2)

print('union of list : ',res)