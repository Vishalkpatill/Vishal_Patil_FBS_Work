## Write a program to convert days into years, weeks and days.

num1 = int(input("Enter the days : "))

year = num1 // 365

num1 = num1 % 365

week = num1 // 7

Remaining_days = num1 % 7

print(f''' Number of year is {year}.
 Number of week is {week}.
 Number of Days is {Remaining_days}.''' )
