import os


def ls():
    while True:
        home = "C:/Users/User/"
        s = input('Введите папку: ')
        if os.path.exists(home + s):
            if os.path.isdir(home + s):
                print(os.listdir(home + s))
            else:
                print("Вы ввели имя не директории, а чего-то другого")
        else:
            print('Объекта(файла/директории) с указанным именем не существует')
        while True:
            continueV = input("Продолжаем? ")
            if continueV == "yes":
                break
            if continueV == "no":
                exit()
            else:
                print('Ответьте yes or no')
                continue


def main():
    ls()

if __name__ == '__main__':
    main()