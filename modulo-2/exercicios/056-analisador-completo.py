# FAZER UM CÓDIGO QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS
# E QUE MOSTRE A MÉDIA DE IDADE
# O NOME DO HOMEM MAIS VELHO
media_idade = 0
mais_velho = 0
cont = 0
for x in range(1, 5):
    print('{:=^20}'.format(f' {x}ª PESSOA '))
    nome = str(input(f'\033[3{x}mQual seu nome: \033[m')).strip()
    idade = int(input(f'\033[3{x}mQual sua idade: \033[m'))
    sexo = str(input(f'\033[3{x}mQual seu sexo [M/F]: \033[m')).upper().strip()
    media_idade += idade
    if x == 1 and sexo == 'M':
        mais_velho = idade
        homen_velho = nome
    if sexo == 'M' and idade > mais_velho:
        homen_velho = nome
        mais_velho = idade
    if sexo == 'F' and idade < 20:
        cont += 1
print('A média das idade do grupo é de {:.0f} anos.'.format(media_idade / 4))
print('O homem o mais velho é o {} e tem {} anos.'.format(homen_velho, mais_velho))
print('São {} mulher com menos de 20 anos.'.format(cont))