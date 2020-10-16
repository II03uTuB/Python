from collections import Counter


def symbols(filename):
    letters = 0
    for line in open(filename):
        letters += len(line)
    print("Letters:", letters)

if __name__ == "__main__":
    s = u"Я учусь в Питере. Здесь странная погода."
    symbols('a.txt')
