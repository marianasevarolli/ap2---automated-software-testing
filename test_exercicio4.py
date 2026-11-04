from unittest.mock import patch
from exercicio4 import criar_identificacao

def test_mensagem():
    with patch("exercicio4.gerar_codigo") as mock:
        mock.return_value = "USR-1234"
        assert criar_identificacao("Carlos") == "Usuário Carlos cadastrado com código USR-1234."

def test_gerar_codigo_chamada():
    with patch("exercicio4.gerar_codigo") as mock:
        criar_identificacao("Carlos")
        mock.assert_called()

def test_chamada_uma_vez():
    with patch("exercicio4.gerar_codigo") as mock:
        criar_identificacao("Carlos")
        mock.assert_called_once()

def test_codigos_diferentes():
    with patch("exercicio4.gerar_codigo") as mock:
        mock.return_value = "USR-9999"
        assert criar_identificacao("Carlos") == "Usuário Carlos cadastrado com código USR-9999."

def test_nomes_diferentes():
    with patch("exercicio4.gerar_codigo") as mock:
        mock.return_value = "USR-1234"
        assert criar_identificacao("Maria") == "Usuário Maria cadastrado com código USR-1234."