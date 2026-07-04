# Write a program to remove all occurrences of a given element in the list.

n = int(input('Enter number to remove from list : '))

li = [1, 2, 3, 2, 4, 5, 2]

li_new = []

for i in li:
    if n != i:
        li_new = li_new + [i]
print(li_new)        