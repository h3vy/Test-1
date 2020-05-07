import TestScan
import scan
import text
import sys
import error
import glob

print('Лексический анализатор языка "MODULA-2"')

def Init():
    i = 1
    if '?' in sys.argv[i]:
        Files = (glob.glob(sys.argv[i]))
        i = 0
        while i < len(Files):
            # print(len(Files))
            text.Reset(Files[i])
            print(i, 'файл:')
            TestScan.Test()
            print()
            i += 1

    elif '*' in sys.argv[i]:
        Files = (glob.glob(sys.argv[i]))
        i = 0
        while i < len(Files):
            text.Reset(Files[i])
            print(i, 'файл:')
            TestScan.Test()
            print()
            i += 1
    else:
        while i < len(sys.argv) :
            text.Reset(sys.argv[i])
            print (i, 'файл:')
            TestScan.Test()
            print()
            i+= 1

if len(sys.argv) < 2:
    error.Error("Запуск: python Mod.py <файл(ы) программы> | *.mod - для всех файлов | ?.mod (количествово '?' = количеству букв в названии) ")


def Done():
    pass

Init()
print()
print("Анализ завершен")
Done()