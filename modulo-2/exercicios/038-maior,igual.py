# Peça dois números e mostre se são maior, menor ou igual

# Pedindo os números
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))

# Vendo qual é o maior, menor ou se são iguais

if n2 == n1:
    print('Os dois números são iguais.')    
elif n1 > n2:
    print(f'O primeirio número é maior.')
else:
    print(f'O segundo número é maior.')
