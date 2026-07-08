# Print 1 to 100 in snakes and ladder pattern.

for row in range(9,-1,-1):
    start = row * 10 + 1
    end = start + 9

    if row % 2 == 0:
        for i in range(start, end + 1):
            print(i, end = ' ')
    else:
        for i in range(end, start - 1, -1):
            print(i,end = ' ')

    print()                