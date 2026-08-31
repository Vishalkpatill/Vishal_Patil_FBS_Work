# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

def findUniqueWords(strings):
    new_words = set()

    for sentence in strings:
        words = sentence.split()
        new_words.update(words)

    return new_words


def countOccurrence(strings, new_words):
    for word in new_words:
        count = 0
        for sentence in strings:
            count += sentence.split().count(word)
        print(word, ":", count)


intro = [
    'my name is Vishal',
    'the name is Vishal',
    'Vishal is a name'
]

unique_words = findUniqueWords(intro)

print("Unique Words:", unique_words)
print("\nFrequency:")

countOccurrence(intro, unique_words)