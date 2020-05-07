# Драйвер исходного текста

import sys
import loc
import error

chEOT = "\0"
chEOL = "\n"
chSPACE = ' '
chTAB = '\t'

_src = ""
_i = 0
_ch = ""


def Reset(i):
    global _src, _i
    loc.pos = 0
    loc.lexPos = 0
    _i = 0
    #if len(sys.argv) < 2:
    #    error.Error("Запуск: python Mod.py <файл программы>")
    #else:
    try:
        _f = open(i)
    except:
        error.Error("Ошибка открытия файла")
    _src = _f.read()
    _f.close()


def nextCh():
    global _src, _i, _ch
    if _i < len(_src):
        _ch = _src[_i]
        print(_ch, end="")
        loc.pos += 1
        _i += 1
        if _ch in {'\n', '\r'}:
            _ch = chEOL
            loc.pos = 0
    else:
        _ch = chEOT


def ch():
    return _ch
