for i in range(1, 6):

    # leading spaces
    for j in range(1, 6 - i):
        print("  ", end="")

    # numbers and hollow spaces
    for j in range(1, i + 1):
        if i == 5 or j == 1 or j == i:
            print(j, end=" ")
        else:
            print("  ", end=" ")

    print()