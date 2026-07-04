# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

li = [10, 20, 30, 40, 20, 50, 20]

n = int(input('Enter number : '))

count = 0

for ele in range(len(li)):
    if li[ele] == n:
        count += 1


if count > 0:
    print(f'{n} element present in list')
    print('count = ', count)
    
else:
    print(f'{n} is not in list')