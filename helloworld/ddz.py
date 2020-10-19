from collections import Counter


def stats(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        strFile = file.read()
    for c, n in sorted(Counter(strFile).items()):
        print(u'{} : {}'.format(c, n))


if __name__ == "__main__":
    s = u"Я учусь в Питере. Здесь странная погода."
    stats('a.txt')
