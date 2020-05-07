# Синтаксический анализатор
from text import *
from scan import *
from table import *


def Test():
    global n, LexDict
    nextCh()
    nextLex()
    n = 0
    LexDict = dict()
    while lex() != Lex.EOT:
        n += 1
        lx = lex()
        if lx in LexDict:
            LexDict[lx] += 1
        else:
            LexDict[lx] = 1
        nextLex()
    print()
    print("Число лексем", n)
    for lx in LexDict:
        print(lx, LexDict[lx], LexDict[lx]/n*100,'%')

