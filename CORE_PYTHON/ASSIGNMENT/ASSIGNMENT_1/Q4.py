## Write a program to enter P, T, R and calculate simple Interest.

num1 = int(input("Enter the P: "))
num2 = int(input("Enter R: "))
num3 = int(input("Enter T: "))

simple_interest = num1 * num2 * num3 / 100

print(f"simple interest for amount {num1} is {simple_interest}rs.")