## Write a program to input any alphabet and check whether it is vowel or consonant.
alpha = input('Enter the alphabet : ')

vowels = "'a','e','i','o','u','A','E','I','O','U'"

if alpha in vowels :
    print('It is vowel')
else :
    print('It is consonant')

 