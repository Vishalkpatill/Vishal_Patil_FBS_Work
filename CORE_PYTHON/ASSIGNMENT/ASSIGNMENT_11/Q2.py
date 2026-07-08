# Python Program to Merge Two Lists and Sort it

def merge_list(li1,li2):
    li1.extend(li2)
    li_merge = li1
    
    li_merge.sort()

    return li_merge

li1 = [2, 4, 7, 8]

li2 = [9, 5, 6, 3, 1]

print('list 1 :',li1)
print('list 2 :',li2)


res = merge_list(li1,li2)

print('Sorterd list :',res)

