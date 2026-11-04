def validar_documento(documento):
    cpf = documento.replace(".", "").replace("-", "")
    return len(cpf) == 11 and cpf.isdigit()