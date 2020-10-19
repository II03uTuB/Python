import matplotlib.pyplot as plt;
import tk as tk
import txt

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
import matplotlib as mpl

mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'


def w_open_ing():
    aa = ord('a')
    bb = ord('z')
    op = askopenfilename()
    main(op, aa, bb)


def w_open_rus():
    aa = ord('а')
    bb = ord('ё')
    op = askopenfilename()
    main(op, aa, bb)


def main(op, aa, bb):
    alpha = [chr(w) for w in range(aa, bb + 1)]  # обратное преобразование кода в символы
    f = open(op, 'r')
    text = f.read()
    f.close()
    alpha_text = [w.lower() for w in text if w.isalpha()]  # выбор только букв и привидение их к нижнему регистру
    k = {}  # создание словаря для подсчета каждой буквы
    for i in alpha:  # заполнение словаря
        alpha_count = 0
        for item in alpha_text:
            if item == i:
                alpha_count = alpha_count + 1
        k[i] = alpha_count
    z = 0
    for i in alpha:  # графическая визуализация данных в поле формы
        z = z + k[i]
    a_a = []
    b_b = []
    t = ('|\tletter\t|\tcount\t|\tpercent,%\t\n')
    txt.insert(END, t)
    t = ('|----------------------------|-----------------------------|---------------------------|\n')
    txt.insert(END, t)
    for i in alpha:  # графическая визуализация данных в поле формы
        persent = round(k[i] * 100.0 / z, 2)
        t = ('|\t%s\t|\t%d\t|\t%s\t\n' % (i, k[i], persent))
        txt.insert(END, t)
        a_a.append(i)
        b_b.append(k[i])
    t = ('|----------------------------|-----------------------------|---------------------------|\n')
    txt.insert(END, t)
    t = ('Total letters: %d\n' % z)
    txt.insert(END, t)
    people = a_a  # подготовка данных для построения диаграммы
    y_pos = np.arange(len(people))
    performance = b_b  # подготовка данных для построения диаграммы
    plt.barh(y_pos, performance)
    plt.yticks(y_pos, people)
    plt.xlabel('Quantity(amount) of the uses of the letter in the text')
    plt.title('The letters of the alphabet')
    plt.show()


def clear_text():
    txt.delete(1.0, END)

    def save_file():
        save_as = asksaveasfilename()
        try:
            x = txt.get(1.0, END)
            f = open(save_as, "w")
            f.writelines(x.encode('utf8'))
            f.close()
        except:
            pass


def close_win():
    if askyesno("Exit", "Do you want to quit?"):
        tk.destroy()


if __name__ == "__main__":
    s = u"Я учусь в Питере. Здесь странная погода."
    symbols('a.txt')
