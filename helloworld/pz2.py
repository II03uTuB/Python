
def shout_on_me():
    while True:
        string = input('Введите строку: \n')
        if string == 'exit':
            exit()
        newString = string.upper()
        print('Полученная строка: ', newString)




if __name__ == '__main__':
    shout_on_me()
