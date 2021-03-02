import uteis


# MODULARIZAÇÃO FOI CRIADA COM OS PRINCIPAIS MOTIVOS
# - PARA DIVIDIR O PROGAMA GRANDE
# - AUMENTAR A LEGIBILIDADE 
# - FACILITAR A MANUTEÇÃO
# - ORGANIZAÇÃO DE CÓDIGO
# - OCCULTAÇÃO DE CÓDIGO PROJETOS

# NA MESMA PASTA TEM UM ARQUIVO CHAMADO UTEIS QUE TEM 3 FUÇÕES
# fatorial(), dobroo() e triplo
# COMO QUALQUER MÓDULO, VAMOS FAZER UMA IMPORTAÇÃO CHAMANDO UTEIS QUE EU MESMO CRIEI
# E PODEMOS USAR TODAS AS FUNÇÕES QUE TEM NO MÓDULO


num = int(input('Digitte um número: '))
fat = uteis.fatorial(num)
dob = uteis.dobro(num)
tri = uteis.triplo(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
print(f'O triplo de {num} é {tri}')


# PACOTE