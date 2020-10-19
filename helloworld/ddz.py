from collections import Counter

import docx
import matplotlib.pyplot as plt
from numpy import save, os


def save(name, fmt):
    pwd = os.getcwd()
    iPath = '.\\'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)


def get_text(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def stats(filename):
    strFile = get_text(filename)
    print(strFile)
    result = sorted(Counter(strFile).items())
    plt.hist(result)
    plt.title('Statistic')
    plt.grid(True)
    save('stats', 'pdf')
    plt.show()


if __name__ == "__main__":
    s = u"Я учусь в Питере. Здесь странная погода."
    stats('timp.docx')
