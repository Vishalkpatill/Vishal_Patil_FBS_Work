# Write a Python program to remove the intersection of a second set
# with a first set.

def intersection(set1, set2):
    set1.difference_update(set2)
    return set1


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70, 80}

res = intersection(set1,set2)
print(res)

