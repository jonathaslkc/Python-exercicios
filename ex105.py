def notas(* n, sit=False):
    """
    ->  Funcao para analisar notas de varios alunos
    :param n: recebe quantidade indetermida de notas de alunos
    :param sit: padrao False, mas caso True, nao calcula situacao
    :return: retorna dicionario com informacoes dos alunos
    """
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n)/len(n)
    if sit:
        if dic['media'] >= 6:
            dic['situacao'] = 'Boa'
        elif dic['media'] >= 5:
            dic['situacao'] = 'Razoável'
        else:
            dic['situacao'] = 'Ruim'
    return dic


# Programa Principal
resp = notas(1, 3.8, 5.9, 7.4, 8, sit=True)
print(resp)
help(notas)
