from helloworld.pz2 import *


def newParser():
    functions = {
        '1': hello,
        'hello': hello,
        '2': shout_on_me,
        'shout_on_me': shout_on_me,
        '3': addCalc,
        'addCalc': addCalc
    }
    flag = True
    while True:
        stringWithFunction = input('Введите название функции:')
        for x in functions.keys():
            if x == stringWithFunction:
                flag = False
        if not flag:
            functions[stringWithFunction]()
        else:
            print('Данной функции в словаре нет!')



if __name__ == '__main__':
    newParser()
