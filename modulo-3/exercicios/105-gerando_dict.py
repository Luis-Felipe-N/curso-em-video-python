def notas(*n, sit=False):
    """
    -> CALCULA NOTA E SITUYAÇÃO DE VÁRIOS ALUNOS
    para *n: recebe várias notas
    para sit: opcional, se quiser mostra o situação
    return: dicionario com várias informação
    """
    dict_notas = {}
    dict_notas['quant_notas'] = len(n)
    dict_notas['maior'] = max(n)
    dict_notas['menor'] = min(n)
    dict_notas['media'] = sum(n) / len(n)
    if sit:
        if dict_notas["media"] < 5:
            dict_notas['sit'] = 'RUIM'
        elif dict_notas['media'] < 7:
            dict_notas['sit'] = 'RAZÓAVEL'
        else:
            dict_notas['sit'] = 'BOA'
    return dict_notas


resp = notas(1, 7, 5, 10, 10, sit=True)
help(resp)