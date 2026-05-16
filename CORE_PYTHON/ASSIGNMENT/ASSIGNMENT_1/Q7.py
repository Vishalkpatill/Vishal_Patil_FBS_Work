## Program to Find the Roots of a Quadratic Equation

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

d = (b**2 - 4*a*c)**0.5

r1 = (-b + d )/(a * 2)
r2 = (-b - d )/(a * 2)

print(f'roots of equations are {r1} and {r2}')


