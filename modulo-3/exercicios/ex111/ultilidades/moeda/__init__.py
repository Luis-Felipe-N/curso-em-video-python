def aumentar(n = 0, p = 0):
    a = n + (n * (p / 100))
    return a

def diminur(n = 0, p = 0):
    d = n - (n * (p / 100))
    return d


def dobro(n = 0):
    n *= 2
    return n


def metade(n = 0):
    n /= 2
    return n


def moeda(n = 0):
    num_format = f'R${n:.2f}'.replace(".", ",")
    return num_format


def resumo(num = 0, aumen = 0 , dimi = 0):
    print('-' *  50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('-' *  50)
    print(f'{"Preço analisado:":<40}{moeda(num):<10}')
    print(f'{"Dobro do preço:":<40}{moeda(dobro(num)):<10}')
    print(f'{"Metade do preço:":<40}{moeda(metade(num)):<10}')
    print(f'{f"Aumentar {aumen}% do preço:":<40}{moeda(aumentar(num, aumen)):<10}')
    print(f'{f"Diminuir {dimi}% do preço:":<40}{moeda(diminur(num, dimi)):<10}')