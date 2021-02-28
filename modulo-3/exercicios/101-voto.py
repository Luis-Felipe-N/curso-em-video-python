from datetime import date

# FAZER UMA FUNÇÃO QUE LEIA COMO PARAMETRO O ANO DE NASCIMENTO E MOSTRE SE A PESSOA PODE OU NÃO VOTAR


def voto(ano=0):
    idade = date.today().year - ano
    if idade < 16:
        frase = f'VOCÊ TEM {idade} ANOS: NÃO VOTA!'
    elif idade < 18 or idade > 70:
        frase = f'VOCÊ TEM {idade} ANOS: VOTO OPCIONAL!'
    else:
        frase = f'VOCÊ TEM {idade} ANOS: VOTO OBRIGATÓRIO!'
        
    return frase


nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))