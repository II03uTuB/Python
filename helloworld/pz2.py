
from helloworld.main import hello

def shout_on_me():
    while True:
        string = input('Введите строку: \n')
        if string == 'exit':
            exit()
        newString = string.upper()
        print('Полученная строка: ', newString)

def addCalc():
    while True:
        sumOfTwoString = input('Введите данные:')
        if sumOfTwoString == 'exit':
            exit()
        flag = True
        if len(sumOfTwoString) == 0:
            print('Введена пустая строка, повторите')
            continue
        for i in sumOfTwoString:
            if i.isdigit():
                continue
            if i == '+':
                continue
            else:
                print('''В строке есть символы, отличные от цифр и знака "+", повторите''')
                flag = False
                break
        if flag:
            listTerms = sumOfTwoString.split('+')
            if len(listTerms) == 2:
                print(float(listTerms[0]) + float(listTerms[1]))
                continue
            else:
                print('Вы указали больше или меньше двух слагаемых')
                continue


def group_parser():
    while True:
        stringWithFunction = input('Введите название функции:')
        stringWithFunction = stringWithFunction.lower()
        if stringWithFunction == 'угадайка':
            hello()
        elif stringWithFunction == 'покричи':
            shout_on_me()
        elif stringWithFunction == 'калькулятор':
            addCalc()
        else:
            print('Нужного пункта меню нет')
            continue



def main():
    group_parser()

if __name__ == '__main__':
    main()
