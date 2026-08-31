# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def find_missing(set1, set2):
    missing_in_second = set1 - set2
    missing_in_first = set2 - set1

    return missing_in_second, missing_in_first


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

missing_second, missing_first = find_missing(set1, set2)

print("Missing in second set:", missing_second)
print("Missing in first set:", missing_first)