from unittest.mock import patch
from exercicio5 import acessar_sistema

def test_com_permissao():
    with patch("exercicio5.verificar_permissao") as mock:
        mock.return_value = True
        assert acessar_sistema("Carlos") == "Acesso autorizado"

def test_sem_permissao():
    with patch("exercicio5.verificar_permissao") as mock:
        mock.return_value = False
        assert acessar_sistema("Carlos") == "Acesso negado"

def test_permissao_chamada():
    with patch("exercicio5.verificar_permissao") as mock:
        acessar_sistema("Carlos")
        mock.assert_called_once()

def test_usuario_correto():
    with patch("exercicio5.verificar_permissao") as mock:
        acessar_sistema("Carlos")
        mock.assert_called_once_with("Carlos")

def test_dois_cenarios():
    with patch("exercicio5.verificar_permissao") as mock:
        mock.return_value = True
        assert acessar_sistema("Ana") == "Acesso autorizado"
        mock.return_value = False
        assert acessar_sistema("Ana") == "Acesso negado"