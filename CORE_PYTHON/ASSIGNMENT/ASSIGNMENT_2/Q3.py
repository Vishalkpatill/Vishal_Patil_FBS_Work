## Convert distance given in feet and inches into meter and centimeter. 

feet = int(input("Enter distance in feet : "))
inches = int(input("Enter distance in inches : "))

centimeter = ((feet * 30) + (inches * 2.54))

meter = centimeter // 100
cm = centimeter % 100
 
print(f'{feet} feet and {inches} inch is {meter} meter and {cm} cm ')


