def obter_proximo_cliente():
    return "Carlos"

def registrar_atendimento(cliente):
    return True

def atender_proximo_cliente():
    cliente = obter_proximo_cliente()
    if not cliente:
        return "Fila vazia"
    if registrar_atendimento(cliente):
        return "Atendimento realizado"
    return "Falha no atendimento"