from helloworld.pz2 import *

def newParser():
    functions = {'hello': hello(), 'shout_on_me': shout_on_me(), 'addCalc': addCalc()}
    while True:
        stringWithFunction = input('Введите название функции:')
        if stringWithFunction ==
