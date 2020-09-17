
def shout_on_me():
    while True:
        string = input('Введите строку: \n')
        if string == 'exit':
            exit()
        newString = string.upper()
        print('Полученная строка: ', newString)

def addCalc():
    while True:
        first = input('Введите первое слагаемое: \n')
        second = input('Введите второе слагаемое: \n')
        if first or second == 'exit':
            exit()




if __name__ == '__main__':
    shout_on_me()
