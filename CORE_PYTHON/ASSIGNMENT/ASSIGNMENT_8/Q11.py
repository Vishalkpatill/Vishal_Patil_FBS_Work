# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.


def count_digits(num):
    count = 0
    temp = num

    while temp > 0:
        count = count + 1
        temp //= 10

    return count


def armstrong_sum(num, digits):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp //= 10

    return total


def is_armstrong(num):
    digits = count_digits(num)
    total = armstrong_sum(num, digits)

    if total == num:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")