import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as element


class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class ReaderJson(Reader):

    def read(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            print(json.load(file))


class ReaderXml(Reader):
    def read(self, filename):
        tree = element.parse(filename)
        root = tree.getroot()

        for elem in root:
            for subElem in elem:
                print(subElem.text)


if __name__ == '__main__':
    j = ReaderXml()
    j.read('data.xml')
