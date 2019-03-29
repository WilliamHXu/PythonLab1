from collections import Counter


def read_shakespeare():
    file = open("longtext.txt", "r").read().lower()
    wordlist = file.split()
    return Counter(wordlist).most_common(250)


print(read_shakespeare())

