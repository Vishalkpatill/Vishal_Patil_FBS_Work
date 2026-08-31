#  8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

def countFrequency(chr):
    word = chr.split()
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1

    return dict 

chr = input('Enter string :')

res = countFrequency(chr)

print(res)