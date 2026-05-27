## WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

num_1 = int(input('enter first number :'))
num_2 = int(input('enter last number : '))

i = num_1

while(i <= num_2):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

    i = i + 1    