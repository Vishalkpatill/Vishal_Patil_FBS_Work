# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

def max_product_pair(numbers):
    pairs = set()
    max_product = None
    max_pair = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair = (numbers[i], numbers[j])
            pairs.add(pair)

    for pair in pairs:
        product = pair[0] * pair[1]

        if max_product is None or product > max_product:
            max_product = product
            max_pair = pair

    return max_pair, max_product


numbers = [2, 5, 3, 8, 1]

pair, product = max_product_pair(numbers)

print("Pair:", pair)
print("Maximum Product:", product)