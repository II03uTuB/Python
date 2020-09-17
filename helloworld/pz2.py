
def shout_on_me():
    while True:
        string = input('Введите строку: \n')
        if string == 'exit':
            exit()
        newString = string.upper()
        print('Полученная строка: ', newString)

def addCalc():
    while True:
        sumOfTwoString = input('Введите данные: \n')
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
            list = sumOfTwoString.split('+')
            if len(list) > 2:
                print('Вы ввели больше двух слагаемых')
                continue
            print(float(list[0]) + float(list[1]))






if __name__ == '__main__':
    addCalc()
