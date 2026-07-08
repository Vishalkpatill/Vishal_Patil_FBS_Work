# Python Program to Sort a List According to the Length of the Elements
# within the list.

def sortLength(li):
    li.sort(key = len)
    return li
    
li = ['lion','dog','elephant','tiger','cheetah']    
print('before sorting :',li)
res = sortLength(li)

print('afeter sorting : ',res)