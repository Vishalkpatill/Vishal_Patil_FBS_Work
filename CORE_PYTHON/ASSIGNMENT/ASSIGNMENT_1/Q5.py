## Write a program to enter P, T, R and calculate Compound Interest.

num1 = float(input("Enter P : "))
num2 = float(input("Enter T :"))
num3 = float(input("Enter R : "))

compound_interest = num1 * (1+(num3/100))**num2 - num1 

print(f"Compound interest for amount {num1}rs is {compound_interest}rs.")