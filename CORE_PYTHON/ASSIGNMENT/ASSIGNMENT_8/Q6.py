# ## 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibb(n):
    a = -1 
    b = 1

    for i in range(n):
        c = a + b
        print(c,end = ' ')
        a = b
        b = c
        
        
n = int(input('enter number : '))
fibb(n)

