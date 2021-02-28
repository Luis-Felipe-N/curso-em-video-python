# # QUANDO VAMOS IMPORTA ALGUNS MÓULOS ELES SEMPRE VEM COM UM MANUAL QUE PODEMOS VÊ-LO COM O CAMANDO help(comando)
# # MAS E NOSSAS FUNÇÃO? PODEMOS CRIA UM MANUAL?
# # SIM DENTRO DA FUNÇÃO PODEMOS ABRIR E FEICHAR 3 " ASPA DUPLAS E INSERIMOS O MANUAL DENTRO DAS ASPAS


# def contador(i, f, p):
#     """
#     para: i inicio
#     para: f fim
#     para: p passo
#     Não retorna nada
#     """
#     c = i
#     while c <= f:
#         print(f'{c} ', end="..")
#         c += p


# # help(contador)

# # PARAMETROS OPCIONAIS
# # JÁ VIMOS QUE PODEMOS PASSAR UM(a), DOIS(a, b), TRÊS(a, b, c) OU INFITOS(*n) PARAMETROS
# # MAS TAMBÉM PODEMOS PASSAR PARAMETROS OPCIONAIS, EM QUE SE O USUÁRIO NÃO PASSAR TODOS OS PARAMETROS
# # O ELE USA O PADRÃO QUE DEFINIRMOS

# def somar(a=0, b=0, c=0):# SE O USUÁRIO NÃO PASSAR O a ELE IRÁ VALER 0, E ASSIM PARA OS OUTROS
#     # OS VALORES DEFINIDOS PODE SER QUALQUER UM
#     soma = a + b + c
#     print(f'A soma valo {soma}')


# somar(c=4)

# # ESCOPO DE VARIÁVEIS
# def teste(b):# RECEBENDO DE PARAMENTRO O a QUE VALE 5
#     global a # INFFORMANDO QUE QUERO USAR O a GLOBAL DENTRO
#     a = 1 # AGORA O a VALE O MESMO VALOR FORA E DENTRO
#     b += 4 # ESCOPO INTERNO
#     c = 10 # ESCOPO INTERNO
#     # COMO DECLARAMOS O b E O c AQUI DENTRO, ELE VAI MOSTRAR OS VALORES DECLARADO
#     print(f'a dentro vale {a}')
#     print(f'b dentro vale {b}')
#     print(f'c dentro vale {c}')
    


# a = 5 # ESCOPO GLOBAL
# teste(a)# PASSANDO COMO PARAMETRO O a QUE VALE 5
# print(f'a fora vale {a}')
# # COMO O b E O c FOI DECLARADO DENTRO DE UMA FUNÇÃO,
# # VAI DAR ERRO POIS ELES NÃO FOI DEFINIDO GLOBALMENTE
#     # print(f'b fora vale {b}')
#     # print(f'c fora vale {c}')


# RETURN
def soma(a=0, b=0, c=0):
    soma = a + b + c
    return soma


r1 = soma(1, 2)
r2 = soma(5, 5)
r3 = soma(4, 9, 2)

print(f'A soma dos 3 valores é {r1} {r2} {r3}')



def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(inputI('Digite um número: '))
