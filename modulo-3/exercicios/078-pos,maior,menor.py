# FAZER UM PROGAMA QUE LEIA 5 NÚMEROS, ADICIONE EM UMA LISTA E MOSTRE:
# OS VALORES DIGITADOS
# O MENOR E O MAIOR
# E SUAS RESPECTIVA POSIÇÕES NO CASO DE MAIS QUE UM NÚMERO MAIOR OU MENOR
   
valores = list()

for pos, v in enumerate(range(0, 4)):
    valores.append(int(input(f'Digite o número da posição {pos}: ')))
print('-' * 30)
print(f'Você digitou os seguintes números: {valores}')

if valores.count(max(valores)) > 1:# SE O NÚMERO DO MAIOR VALOR FOR MAIS QUE 1 
    print(f'O maior número digitado foi {max(valores)} nas posições ', end="")
else:
    print(f'O maior número digitado foi {max(valores)} na posição ', end="")
for p,n in enumerate(valores):
    if n == max(valores):
        print(f'{p}... ', end=" ")

if valores.count(min(valores)) > 1:# SE O NÚMERO DO MENOR VALOR FOR MAIS QUE 1
    print(f'\nO menor número digitado foi o {min(valores)} nas posições ', end="")
else:
    print(f'\nO menor número digitado foi o {min(valores)} na posição ', end="")
for p,n in enumerate(valores):
    if n == min(valores):
        print(f'{p}... ', end="")