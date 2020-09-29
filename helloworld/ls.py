import os


def ls():
    while(True):
        s = input('Введите папку: ')
        #dirLists = os.listdir("C:")
        print(os.listdir("C:" + s))

        while True:
            continueV = input("Продолжаем?")
            if continueV == ("yes" or "да" or "1"):
                break
            elif continueV == ("no" or "нет" or "0"):
                exit()
            else:
                print('Ответьте да\нет, yes\/no, 1/2')
                continue
