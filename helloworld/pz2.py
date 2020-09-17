
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
        if not sumOfTwoString:
            print('Строка пуста, повторите')
            continue
        if sumOfTwoString == 'exit':
            exit()
        if not sumOfTwoString.isspace():
            print('в строке присутствуют символы, отличные от цифр и знака "+", повторите')
            continue

        list = sumOfTwoString.split('+')
        if len(list) > 2:
            print('Вы ввели больше двух слагаемых')
            continue
        print(float(list[0]) + float(list[1]))






if __name__ == '__main__':
    addCalc()
