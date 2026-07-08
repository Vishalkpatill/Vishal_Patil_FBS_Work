# Write a program to print list after removing even numbers.

def removeEven(li):
    li1 = []
    for i in li:
        if i % 2 != 0:
            li1.append(i)

    return li1

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

res = removeEven(li)

print(res)