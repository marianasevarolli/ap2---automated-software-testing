from exercicio1 import *

def test_sem_estoque():
    assert classificar_produto(0) == "Sem estoque"

def test_estoque_baixo():
    assert classificar_produto(3) == "Estoque baixo"

def test_estoque_normal():
    assert classificar_produto(10) == "Estoque normal"

def test_estoque_alto():
    assert classificar_produto(30) == "Estoque alto"

def test_quantidade_negativa():
    assert classificar_produto(-1) == "Quantidade inválida"