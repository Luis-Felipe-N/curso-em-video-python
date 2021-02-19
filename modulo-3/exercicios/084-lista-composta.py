# FAZER UM PROGAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS GUARDANDO TUDO EM UMA LISTA NO FINAL MOSTRE:
# QUANTAS PESSOAS FORAM CADASTRADAS.
# UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
# UMA LISTAGEM COM AS PESSOAS MAIS LEVES

pessoas = list()
dados = []
maior = menor = 0 
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        elif menor > dados[1]:
            menor = dados[1]
    pessoas.append(dados[:])# FAZENDO UMA COPIA PARA A LISTA PESSOAS NÃO SOFRA ALTERAÇÃO
    dados.clear()
    cont = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    while cont not in "sn":
        cont = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if cont == 'n':
        break

print('-' * 33)
print(f'{len(pessoas)} pessoas foram cadastradas.')

print(f'O maior peso foi {maior}. Peso do ', end="")
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end="")
print(f'\nO menor peso foi {menor}.Peso do ', end="")
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end="")