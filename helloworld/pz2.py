
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
        ptr = True
        for i in sumOfTwoString:
            if i.isdigit():
                continue
            if i == '+':
                continue
            else:
                print('''В строке присутствуют символы, отличные 
                                            от цифр и знака "+" или же недостаточно данных для действия, повторите''')
                ptr = False
                break
        if ptr == True:
            list = sumOfTwoString.split('+')
            if len(list) > 2:
                print('Вы ввели больше двух слагаемых')
                continue
            print(float(list[0]) + float(list[1]))


#f not sumOfTwoString:
        #   print('Строка пуста, повторите')
         #   continue

        #if sumOfTwoString.isalpha():
        #    print('''В строке присутствуют символы, отличные
        #    от цифр и знака "+" или же недостаточно данных для действия, повторите''')
         #   continue








if __name__ == '__main__':
    addCalc()
