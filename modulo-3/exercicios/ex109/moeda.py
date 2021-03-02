def aumentar(n, p, formatacao = True):
    a = n + (n * (p / 100))
    if formatacao:
        a = moeda(a)
    return a

def diminur(n , p, formatacao = True):
    d = n - (n * (p / 100))
    if formatacao:
        d = moeda(d)
    return d


def dobro(n, formatacao = True):
    n *= 2
    if formatacao:
        n = moeda(n)
    return n


def metade(n, formatacao = True):
    n /= 2
    if formatacao:
        n = moeda(n)
    return n


def moeda(n):
    num = f'R${n:.2f}'.replace(".", ",")
    return num