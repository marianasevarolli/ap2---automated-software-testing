from exercicio2 import *

def test_varias_palavras():
    assert inverter_palavras("Python é muito interessante") == "interessante muito é Python"

def test_uma_palavra():
    assert inverter_palavras("Python") == "Python"

def test_frase_vazia():
    assert inverter_palavras("") == ""

def test_espacos_extras():
    assert inverter_palavras("  Python   é   legal  ") == "legal é Python"

def test_numeros_e_letras():
    assert inverter_palavras("abc 123 def 456") == "456 def 123 abc"