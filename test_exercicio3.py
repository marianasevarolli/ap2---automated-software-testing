from exercicio3 import *

def test_11_digitos():
    assert validar_documento("12345678900") == True

def test_formatado():
    assert validar_documento("123.456.789-00") == True

def test_menos_de_11():
    assert validar_documento("12345") == False

def test_mais_de_11():
    assert validar_documento("123456789012") == False

def test_com_letras():
    assert validar_documento("1234567890a") == False

def test_vazio():
    assert validar_documento("") == False