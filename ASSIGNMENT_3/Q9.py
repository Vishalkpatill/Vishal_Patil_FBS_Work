## Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input('Marathi : '))
sub2 = int(input('Hindi : '))
sub3 = int(input('English :'))
sub4 = int(input('Math : '))
sub5 = int(input('So-sci : '))

total = (sub1 + sub2 + sub3 + sub4 + sub5)

if total >= 300 and total <= 500 :
    print('First class')
elif total < 300 and total >= 250 :
    print("Second class")
elif total < 250 and total >= 172 :
    print('Third class')
else :
    print('Fail')        

 


        