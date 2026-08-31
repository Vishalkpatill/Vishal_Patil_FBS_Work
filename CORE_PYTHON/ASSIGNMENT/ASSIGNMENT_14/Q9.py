# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def combinations(numbers, target):
    combinations = set()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                
                if numbers[i] + numbers[j] + numbers[k] == target:
                    combination = (numbers[i], numbers[j], numbers[k])
                    combinations.add(combination)

    return combinations


numbers = [1, 2, 3, 4, 5, 6]
target = 9

result = combinations(numbers, target)

print("Combinations:", result)