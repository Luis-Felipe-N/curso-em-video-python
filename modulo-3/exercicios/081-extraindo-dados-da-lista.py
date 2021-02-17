# FAZER UM PROGAMA QUE LEIA VÁRIOS NÚMEROS E COLOCAR EM UMA LISTAE MOSTRE:
# QUANTOS NÚMEROS FORAM DIGITADOS
# A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE
# SE O VALOR ESTÁ OU NÃO NA LISTA

valores = list()
while True:
    valores.append(int(input('Digite um número :\033[32m \033[m')))
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você digitou {len(valores)} números')

valores1 = valores[:]
# SE COLOCARMOS valores1 = valores, QUALQUER ALTERAÇÃO QUE FAZER NA VARÍAVEL valores1 TAMBÉM VAI MUDAR EM valores.
# ISSO PORQUE ELES TEM UMA LIGAÇÃO, AO COLOCARMOS [:] ESSE LIGAÇÃO SE CORTA
# PODEMOS USAR TAMBÉM O copy()
valores1.sort(reverse=True)
print(f'A lista na ordem decrescente é {valores1}')

if valores.count(5) >= 1:
    print(f'O 5 está na lista na posição {valores.index(5)}')
