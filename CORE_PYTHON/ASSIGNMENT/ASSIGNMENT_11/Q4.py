# 4. Python Program to Find the Second Largest Number in a List Using Bubble sort

def find2ndLargestEle(li):

    n = len(li)
    for i in range(n):
        for j in range (n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    return li[-2]            
                
    
li = [15, 21, 10, 12, 30, 10]    

res = find2ndLargestEle(li)           

print('2nd largest ele :',res)



    