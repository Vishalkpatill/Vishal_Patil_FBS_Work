# Write a program to print all numbers which are divisible by m and n in the
# list.

m = int(input('Enter m : '))
n = int(input('Enter n : '))

li = [5, 10, 16, 20, 25, 31, 35, 41, 46, 50]



for i in li:
    if i % m == 0 and i % n == 0:
        print(i)
else:
    print(f'Numbers present in the list is divisible by {m} and {n}.')