# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

n = int(input('Enter number :'))

li_even = []

li_odd = []

for i in range(1, n + 1):
    if i % 2 == 0:
        li_even = li_even + [i]
    else:
        li_odd = li_odd + [i]

print(li_even)
print(li_odd)
