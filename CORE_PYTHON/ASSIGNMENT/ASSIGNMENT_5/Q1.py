#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

uid = (input('enter user id : '))
passw = int(input('enter password : '))

user = "vishal"
password = 1234

if uid == user and passw == password:
    print('log in success')

    i = 1
    while(i <= 3):
        if passw == password:
            print(f'{passw} is correct')
            break
        i += 1
    else:
        print('wrong password')