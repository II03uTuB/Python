from helloworld.pz2 import *


def newParser():
    functions = {
        'hello': hello,
        'shout_on_me': shout_on_me,
        'addCalc': addCalc
    }
    while True:
    stringWithFunction = input('Введите название функции:')
    #x = functions.get(stringWithFunction)
    functions[stringWithFunction]()
    # functions.keys(stringWithFunction)

    functions[x]()

    # if stringWithFunction ==


if __name__ == '__main__':
    newParser()
