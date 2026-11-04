from unittest.mock import patch
from exercicio6 import atender_proximo_cliente

def test_sucesso():
    with patch("exercicio6.obter_proximo_cliente") as obter, patch("exercicio6.registrar_atendimento") as registrar:
        obter.return_value = "Carlos"
        registrar.return_value = True
        assert atender_proximo_cliente() == "Atendimento realizado"

def test_fila_vazia():
    with patch("exercicio6.obter_proximo_cliente") as obter:
        obter.return_value = None
        assert atender_proximo_cliente() == "Fila vazia"

def test_falha():
    with patch("exercicio6.obter_proximo_cliente") as obter, patch("exercicio6.registrar_atendimento") as registrar:
        obter.return_value = "Carlos"
        registrar.return_value = False
        assert atender_proximo_cliente() == "Falha no atendimento"

def test_obter_chamada():
    with patch("exercicio6.obter_proximo_cliente") as obter, patch("exercicio6.registrar_atendimento"):
        obter.return_value = "Carlos"
        atender_proximo_cliente()
        obter.assert_called_once()

def test_registrar_cliente_correto():
    with patch("exercicio6.obter_proximo_cliente") as obter, patch("exercicio6.registrar_atendimento") as registrar:
        obter.return_value = "Carlos"
        atender_proximo_cliente()
        registrar.assert_called_once_with("Carlos")

def test_registrar_nao_chamado():
    with patch("exercicio6.obter_proximo_cliente") as obter, patch("exercicio6.registrar_atendimento") as registrar:
        obter.return_value = None
        atender_proximo_cliente()
        registrar.assert_not_called()