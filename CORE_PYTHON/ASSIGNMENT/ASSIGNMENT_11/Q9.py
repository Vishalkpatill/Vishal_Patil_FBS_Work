# Write a program to create three lists of numbers, their squares and cubes

def listOf3(li):
    li_sq = []
    li_cu = []

    for i in li:
        li_sq.append(i ** 2)
        li_cu.append(i ** 3)

    return li,li_sq,li_cu    
    

li = [2, 4, 5, 6, 7, 8, 9, 10]

num, sqr, cube = listOf3(li)

print('list of number :',num)
print('list of square :',sqr)
print('list of cube :',cube)