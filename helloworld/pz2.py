
def shout_on_me():
    while True:
        # print('Введите строку')
        str = input('Введите строку: \n')
        if str == 'exit' :
            exit()
        for x in str:
            x.upper()
        print('Полученная строка: ', str)




if __name__ == '__shout_on_me()__':
    shout_on_me()
