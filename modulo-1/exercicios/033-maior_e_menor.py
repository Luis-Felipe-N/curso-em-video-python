# Fazer um progama que peça três números e mostre o maior e o menor

# Pedi os três números
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

# Mostrar qual níumero é o maior e o menor

# Vendo quem é o menor número
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

# Vendo quem é o maior número
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print(f'O menor numero é o {menor}.')
print(f'O maior número é o {maior}.')