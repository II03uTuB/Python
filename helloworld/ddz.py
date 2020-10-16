from collections import Counter
from string import ascii_letters


def symbols(filename):
    with open(filename) as file:
        text = file.read().splitlines()
        dic = {}
        for x in ascii_letters:
            dic[x] = text.count(x)
    print(dic)


if __name__ == "__main__":
    s = u"Я учусь в Питере. Здесь странная погода."
    symbols('a.txt')
