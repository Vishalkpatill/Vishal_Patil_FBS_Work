## 9. WAP to print all numbers in a range divisible by a given number 

start = int(input('enter number : '))
end = int(input('enter number : '))

num = int(input('enter number to divide : '))


while (start <= end):
    if start % num == 0:
        print(start)
    start += 1    