def aumentar(n, p):
    a = n + (n * (p / 100))
    return a


def diminur(n , p):
    d = n - (n * (p / 100))
    return d


def dobro(n):
    n *= 2
    return n


def metade(n):
    n /= 2
    return n


def moeda(n):
    num = f'R${n:.2f}'.replace(".", ",")
    return num