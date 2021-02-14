# Fazer um progama que leia um número e mostre na tela se ele é impar ou par

# Pedir o número ao usuário
numero = int(input('Digite um número: '))

# Número impar ou par
#OBSERVACÃO: Todo número par dividido por 2 o resto é zero e o que não for é par
resto = numero % 2

# Motre se ele é impa ou par
if resto == 0:
    print('O número é par!')
else:
    print('O número é impar!')

