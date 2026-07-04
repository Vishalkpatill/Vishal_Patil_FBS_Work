# Write a program to create a new list from existing list which contains cube of
# each number of list.

li = [1, 2, 3, 4, 5]

new_li = [0] * len(li)

for i in range(len(li)):
    new_li[i] = li[i] ** 3

print(new_li)    