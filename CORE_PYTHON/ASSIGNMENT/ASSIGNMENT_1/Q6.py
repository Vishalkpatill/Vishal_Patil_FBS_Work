## Write a Program to input two angles from user and find third angle of the triangle.
num1 = int(input("Enter angle 1 : "))
num2 = int(input("Enter angle 2 : "))

third_angle = 180 - num1 - num2

print(f"Third angle of triangle is {third_angle}.")