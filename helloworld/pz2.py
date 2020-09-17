
def shout_on_me():
    global upperStr
    while True:
        # print('Введите строку')
        str = input('Введите строку: \n')
        if str == 'exit' :
            exit()
        #for x in str:
        newStr = str.upper()
        print('Полученная строка: ', newStr)




if __name__ == '__main__':
    shout_on_me()
