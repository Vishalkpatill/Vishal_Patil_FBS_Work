# Write a Python program to find elements in a given set that are not in
# another set.

def removeElement(set1, set2):

    return set1.difference(set2)
    

set1 = {10, 20, 30, 40, 50, 60, 70, 80}
set2 = {30, 40, 50, 60, 70}

res = removeElement(set1, set2)

print(res)

