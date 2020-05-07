import string
from enum import Enum

from text import *
from error import *

c = 13
n = 102
BASE = 17
index = 0


class Item():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.free = 0


class HashTable:
    def hash(self, key):
        global n
        s = 0
        for i in range(1, len(key)):
            s = BASE * s + ord(key[i])
        return (abs(s) % n)

    def __init__(self):
        global n
        self.H = [0] * n
        self.CreateLexTable()

    def AddToHash(self, key, value):
        global n
        h = self.hash(key)
        Q = False
        Item1 = Item('1', '0')
        while Q != True:
            if self.H[h] == 0:
                Item1.key = key
                Item1.value = value
                Item1.free = False
                self.H[h] = Item1
                Q = True
            elif key != self.H[h].key:
                h = (h + c) % n
            else:
                Q = True

    def Get(self, key, value):
        index = self.HashSearch(key)
        if index == -666:
            return value
        else:
            return self.H[index].value

    def HashSearch(self, key):
        global n
        h = self.hash(key)
        Q = False
        while Q != True:
            if self.H[h] == 0:
                Q = True
                index = -666
            elif key == self.H[h].key:
                Q = True
                index = h
            else:
                h = (h + c) % n
        return index

    def CreateLexTable(self):
        self.AddToHash('IMPORT', Lex.IMPORT)
        self.AddToHash("CONST", Lex.CONST)
        self.AddToHash("VAR", Lex.VAR)
        self.AddToHash("BEGIN", Lex.BEGIN)
        self.AddToHash("END", Lex.END)
        self.AddToHash("IF", Lex.IF)
        self.AddToHash("THEN", Lex.THEN)
        self.AddToHash("ELSIF", Lex.ELSIF)
        self.AddToHash("ELSE", Lex.ELSE)
        self.AddToHash("WHILE", Lex.WHILE)
        self.AddToHash("DO", Lex.DO)
        self.AddToHash("DIV", Lex.DIV)
        self.AddToHash("MOD", Lex.MOD)
        self.AddToHash("ARRAY", Lex.ARRAY) ##
        self.AddToHash("RECORD", Lex.RECORD)
        self.AddToHash("POINTER", Lex.POINTER)
        self.AddToHash("SET", Lex.SET)
        self.AddToHash("WITH", Lex.WITH)
        self.AddToHash("CASE", Lex.CASE)
        self.AddToHash("OF", Lex.OF)
        self.AddToHash("LOOP", Lex.LOOP)
        self.AddToHash("EXIT", Lex.EXIT)
        self.AddToHash("PROCEDURE", Lex.PROCEDURE)
        self.AddToHash("FOR", Lex.FOR)
        self.AddToHash("TO", Lex.TO)
        self.AddToHash("BY", Lex.BY)
        self.AddToHash("IN", Lex.IN)
        self.AddToHash("IS", Lex.IS)
        self.AddToHash("NIL", Lex.NIL)
        self.AddToHash("OR", Lex.OR)
        self.AddToHash("TYPE", Lex.TYPE)
        self.AddToHash("REPEAT", Lex.REPEAT)
        self.AddToHash("UNTIL", Lex.UNTIL)
        self.AddToHash("RETURN", Lex.RETURN)
        self.AddToHash("MODULE", Lex.MODULE)
        self.AddToHash("DEFINITION", Lex.DEFINITION)
        self.AddToHash("POINTER", Lex.POINTER)
        self.AddToHash("AND", Lex.AND)
        self.AddToHash("SET", Lex.SET)
        self.AddToHash("BY", Lex.BY)
        self.AddToHash("EXPORT", Lex.EXPORT)
        self.AddToHash("NOT", Lex.NOT)
        self.AddToHash("CASE", Lex.CASE)
        self.AddToHash("FOR", Lex.FOR)
        self.AddToHash("OF", Lex.OF)
        self.AddToHash("TO", Lex.TO)
        self.AddToHash("FROM", Lex.FROM)
        self.AddToHash("OR", Lex.OR)
        self.AddToHash("IMPLEMENTATION", Lex.IMPLEMENTATION)
        self.AddToHash("QUALIFIED", Lex.QUALIFIED)
        self.AddToHash("IN", Lex.IN)
        self.AddToHash("RECORD", Lex.RECORD)
        self.AddToHash("WITH", Lex.WITH)


class Lex(Enum):
    NONE, NAME, NUM, MODULE, IMPORT, BEGIN, END, EXIT, CONST, DEFINITION, IF, POINTER, \
    VAR, WHILE, REPEAT, DO, ARRAY, RETURN,  THEN, ELSIF, ELSE, AND, MULT, DIV, MOD, \
    PLUS, MINUS, EQ, NE, LT, LE, GT, GE, DOT, COMMA, SET, BY, EXPORT, NOT, CASE, \
    FOR, OF, TO, FROM, LOOP, OR, TYPE, COLON, SEMI, ASS, LPAR, RPAR, \
    UNTIL, IMPLEMENTATION, PROCEDURE, QUALIFIED, IN, RECORD, WITH, EOT, IS, NIL, \
    DOBDOT, DEL, LOGI, ILPAR, IRPAR, RAZ, lRPAR, rLPAR, CHAR, LOGN, AP, CAW, FLOAT, INT = range(76)


MAX = 0x7FFFFFFF
MAXREAL = 0x7FFFFFFF

_lex = Lex.NONE
_num = 0
_name = ""

_kw = HashTable()

_names = {
    Lex.NAME: 'имя',
    Lex.NUM: 'число',
    Lex.MULT: '"*"',
    Lex.PLUS: '"+"',
    Lex.MINUS: '"-"',
    Lex.EQ: '"="',
    Lex.NE: '"#"',
    Lex.LT: '"<"',
    Lex.LE: '"<="',
    Lex.GT: '">"',
    Lex.GE: '">="',
    Lex.DOT: '"."',
    Lex.COMMA: '","',
    Lex.COLON: '":"',
    Lex.SEMI: '";"',
    Lex.ASS: '":="',
    Lex.LPAR: '"("',
    Lex.RPAR: '")"',
    Lex.DOBDOT: '".."',
    Lex.DEL: '"/"',
    Lex.LOGI:'"&"',
    Lex.LOGN:'"~"',
    Lex.ILPAR: '"["',
    Lex.IRPAR: '"]"',
    Lex.RAZ: '"^"',
    Lex.rLPAR: '"}"',
    Lex.lRPAR: '"{"',
    #Lex.AP:"'",
    #Lex.CAW: '"'
}


def lexName(L):
    return _names.get(L, L.name)


def scanIdent():
    global _lex, _name
    _name = ch()  # Первая буква
    nextCh()
    while ch() in string.ascii_letters + string.digits:
        _name += ch()
        nextCh()
    _lex = _kw.Get(_name, Lex.NAME)


def scanNumber():
    global _num, _lex
    _num = 0;
    dec = False
    hec = False
    t_char = False
    float = False
    while ch() in string.digits:
        if  '0' <= ch() <= '7':
            if _num <= (MAX - int(ch())) // 10:
                _num = 10 * _num + int(ch())
            else:
                lexError("Слишком большое число")
        else:
            dec = True
            #break
            if ch() in {'8','9'}:
                if _num <= (MAX - int(ch())) // 10:
                    _num = 10 * _num + int(ch())
                else:
                    lexError("Слишком большое число")

        nextCh() ## Целая часть

    if ch() in {'B','b'}:
        nextCh()
        if dec and (ch() == ' ' or ch() == chEOT):
            lexError('Такое число не существует в 8 с.с. ')
        if ((ch() in string.digits) or ('A' <= ch() <= 'F') or ('a' <= ch() <= 'f')):
            while ((ch() in string.digits) or ('A' <= ch() <= 'F') or ('a' <= ch() <= 'f')):
                nextCh()
            if ch() != 'H':
                lexError('При записи числа в 16 системе счисления должна быть указана буква "H" ')
            else:
                nextCh()
        if ch() == 'H':
            hec = True
            nextCh()
    elif ch() == 'H':
        nextCh()
        hec = True
        #if ((ch() in string.digits)) or (ch() in string.ascii_letters):
        #    lexError('За 16-ичным числом не может следовать символ')

    elif ch() in {'C','c'} and dec == False:
        nextCh()
        if ch() == ' ' or ch() == chEOT or ch() == chEOL:
            t_char = True
        elif ch() == 'H':
            nextCh()
            hec = True



    if ((ch() in string.digits) or ('A' <= ch() <= 'F') or ('a' <= ch() <= 'f')) and hec == False:
        while (ch() in string.digits) or ('A' <= ch() <= 'F') or ('a' <= ch() <= 'f'):
            nextCh()
        if ch() == 'H':
            nextCh()
        else:
            lexError('При записи числа в 16 системе счисления должна быть указана буква "H" ')

    degree = 0
    if ch() == '.':
        dec = True

    if (ch() == '.') and dec: ## Вещественная
        nextCh()
        while ch() in string.digits:
            degree -= 1
            if _num <= (MAX - int(ch())) // 10:
                _num = _num + int(ch()) * 10**degree
                round(_num, degree * (-1))
            else:
                lexError("Слишком большое число")
            nextCh()
        _num = round(_num, degree * (-1))
        float = True
    if (ch() == 'E') and dec: ## Проверяем экспоненту
        float = True
        nextCh()
        sgne = 0
        enumb = 0
        if ch() == '-':
            sgne = -1
            nextCh()
        else:
            if ch() in string.digits:
                sgne = 1
        if sgne != 0:
            while ch() in string.digits:
                if enumb <= (MAX - int(ch())) // 10:
                    enumb = 10 * enumb + int(ch())
                else:
                    lexError("Слишком большое число")
                nextCh()
            enumb = sgne * enumb # Степень Е
            _num = _num * 10 ** enumb # Число в степени E
            _num = round(_num,(enumb + degree) * (-1)) # Учитываем кол-во знаков после запятой у EXP и самого числа
        else:
            lexError("Ожидается степень экспоненты")
    if t_char:
        _lex = Lex.CHAR
    elif float:
        _lex = Lex.FLOAT
    else:
        _lex = Lex.INT


def Comment():
    nextCh()  # *
    while True:
        while ch() not in {'*', chEOT, '('}:
            nextCh()
        if ch() == chEOT:
            lexError("Не закончен комментарий")
        elif ch() == '*':
            nextCh()
            if ch() == ')':
                nextCh()
                break
        else:
            nextCh()
            if ch() == '*':
                Comment()


def nextLex():
    global _lex

    while ch() in {chSPACE, chTAB, chEOL}:
        nextCh()

    loc.lexPos = loc.pos

    if ch() in string.ascii_letters:
        scanIdent()
    elif ch() in string.digits:
        scanNumber()
    elif ch() == ';':
        _lex = Lex.SEMI
        nextCh()
    elif ch() == '(':
        nextCh()
        if ch() == '*':
            Comment()
            nextLex()
        else:
            _lex = Lex.LPAR
    elif ch() == ')':
        _lex = Lex.RPAR
        nextCh()
    elif ch() == ',':
        _lex = Lex.COMMA
        nextCh()
    elif ch() == '.':
        _lex = Lex.DOT
        nextCh()
        if ch() == '.':
            _lex = Lex.DOBDOT
            nextCh()
    elif ch() == ':':
        nextCh()
        if ch() == '=':
            _lex = Lex.ASS
            nextCh()
        else:
            _lex = Lex.COLON
        nextCh()
    elif ch() == '>':
        nextCh()
        if ch() == '=':
            _lex = Lex.GE
            nextCh()
        else:
            _lex = Lex.GT
    elif ch() == '<':
        nextCh()
        if ch() == '=':
            _lex = Lex.LE
            nextCh()
        if ch() == '>':
            _lex = Lex.NE
            nextCh()
        else:
            _lex = Lex.LT
    elif ch() == '=':
        _lex = Lex.EQ
        nextCh()
    elif ch() == '#':
        _lex = Lex.NE
        nextCh()
    elif ch() == '+':
        _lex = Lex.PLUS
        nextCh()
    elif ch() == '-':
        _lex = Lex.MINUS
        nextCh()
    elif ch() == '*':
        _lex = Lex.MULT
        nextCh()
    elif ch() == '/':
        _lex = Lex.DEL
        nextCh()
    elif ch() == '&':
        _lex = Lex.LOGI
        nextCh()
    elif ch() == '~':
        _lex = Lex.LOGN
        nextCh()
    elif ch() == '[':
        _lex = Lex.ILPAR
        nextCh()
    elif ch() == ']':
        _lex = Lex.IRPAR
        nextCh()
    elif ch() == '^':
        _lex = Lex.RAZ
        nextCh()
    elif ch() == '{':
        _lex = Lex.rLPAR
        nextCh()
    elif ch() == '}':
        _lex = Lex.lRPAR
        nextCh()
    elif ch() == "'":
        nextCh()
        while ch() not in {"'",chEOL}:
            #print(ch())##########
            nextCh()
        if ch() == "'":
            nextCh()
        else:
            lexError("Ожидается завершающий символ")
        _lex = Lex.AP
    elif ch() == '"':
        nextCh()
        while ch() not in {'"', chEOL}:
            #print(ch())#######
            nextCh()
        if ch() == '"':
            nextCh()
        else:
            lexError("Ожидается завершающий символ")
        _lex = Lex.CAW

    elif ch() == chEOT:
        _lex = Lex.EOT
    else:
        lexError("Недопустимый символ")


def lex():
    return _lex


def name():
    return _name


def num():
    return _num