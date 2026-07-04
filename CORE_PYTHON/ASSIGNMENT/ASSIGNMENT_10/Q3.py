# 3. Write a program to find the second largest element in the list.

li = [10, 80, 60, 50, 70]

max = smax = float('-inf')

for i in range(0, len(li)):
    if(li[i] > max):
        smax = max
        max = li[i]
    elif(li[i] > smax):
        smax = li[i]

print('maximum:', max) 
print('second maximum', smax)       
