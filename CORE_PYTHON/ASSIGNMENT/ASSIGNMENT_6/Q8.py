for i in range(1, 6):

    
    for j in range(5 - i):
        print(" ", end=" ")

    ch = 'A'

    
    for k in range(2 * i - 1):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)

    print()