## Write a program to check if user has entered correct userid and password.

user = int(input('Enter userid : '))
pswd = input('Enter password : ')

userid = 1234

password = ('Vishal123')

if (user == userid) and (pswd == password) :
    print('log in successful')
else :
    print('invalid userid or password')

