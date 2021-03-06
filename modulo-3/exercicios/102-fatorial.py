# FAZER UMA FUNÇÃO QUE CALCULE O FATORIAL DE UM NÚMERO INTEIRO
# E CONFORME O PARAMETRO PASSADO A FUNÇÃO MOSTRA O CALCULO FEITO

def fatorial(n, show=False):
    """
    -> CALCULE FATORIAL DE UM NÚMERO
    para n: n é o número que será calculado o fatorial
    para show: se show:True vai mostrar o calculo
    return: vai retornar o n fatorado
    """
    f = 1
    while n != 0:
        if show:
            if n != 1:
                print(f'{n} x ', end="")
            if n == 1:
                print(f'{n} = ', end="")
        f *= n
        n -= 1
    return f


print(fatorial(70, True))
