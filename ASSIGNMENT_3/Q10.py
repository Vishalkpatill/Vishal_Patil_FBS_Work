## Write a program to check if person is eligible to marry or not (male age >=21 and
## female age>=18)

gen = input('Enter gender (M/F) : ')

age = int(input('Enter age : '))

if gen == 'M' :
    if age >= 21 :
        print('Eligible for marriage')
    else :
        print('Not eligible')
else : 
    if age >= 18 :
        print('eligible for marriage')
    else: print('NOt eligible')