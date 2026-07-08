# Python Program to Find the Intersection of Two Lists

def intersection(li1,li2):
    inter = list(set(li1) & set(li2))
    return inter

li1 = [1, 2, 3, 4]
li2 = [2, 3, 4, 5]

res = intersection(li1,li2)

print('intersection of list :',res)