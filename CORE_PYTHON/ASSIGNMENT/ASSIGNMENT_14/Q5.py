# Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

def longPrefix(string):
    short = min(string, key= len)
    prefix = ''

    for i in range(len(short)):
        char = set()

        for stri in string:
            char.add(stri[i])

        if len(char) == 1:
            prefix = prefix + short[i]
        else:
            break
    return prefix

string = ['flower', 'flow', 'flight']

print('longest common prefix :', longPrefix(string))