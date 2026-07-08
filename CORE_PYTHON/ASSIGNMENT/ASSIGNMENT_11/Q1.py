## 1. Python Program to Put Even and Odd elements of a List into two Different list

def odd_even(li):
    li_even = []
    li_odd = []

    for num in li:
        if num % 2 == 0:
            li_even.append(num)
        else:
            li_odd.append(num)

    return li_even, li_odd

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even,odd = odd_even(li)


print('Even list', even)

print('Odd list', odd)
