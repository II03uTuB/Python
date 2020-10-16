import json
from abc import ABC, abstractmethod

import xml.dom.mimidom

class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class ReaderJson(Reader):

    def read(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            print(json.load(file))


class ReaderXml(Reader):
    def read(self, filename, tag):
        tree = xml.ElementTree(tag)
        with open(filename, "w") as fh:
            tree.write(fh)



if __name__ == '__main__':
    j = ReaderJson()
    j.read('data.json')