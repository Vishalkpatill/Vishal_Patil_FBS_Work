# 3. Python Program to Detect if Two Strings are Anagrams

def anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

string1 = input('Enter string 1 :') 
string2 = input('Enter string 2 :')

if anagrams(string1, string2):
    print('it is anagram')
else:
    print('not anagram')
