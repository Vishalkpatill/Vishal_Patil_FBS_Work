# Write a program to find maximum and minimum element in a list.

li = [20, 30, 10, 50, 40]

min = float('inf')
max = float('-inf')
for i in range(len(li)):
    if li[i] < min:
        min = li[i]
    
    if li[i] > max:
        max = li[i]

print('min : ', min)
print('max', max)        
