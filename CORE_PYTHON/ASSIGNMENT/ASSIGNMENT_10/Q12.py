# Write a program to create three lists of numbers, their squares
# and cubes

li = [1, 2, 3, 4, 5]

li_sq = []

li_cu = []

for i in (li):
    li_sq = li_sq + [i ** 2]
    li_cu = li_cu + [i ** 3]

print(li_sq) 
print(li_cu)   