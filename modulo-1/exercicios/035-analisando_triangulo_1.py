# Fazer um progama que leia três retas e mostre se é possível a existencia de um triangulo

# Ler as três retas
reta_a = float(input('Qual o comprimento da reta A em cm: '))
reta_b = float(input('Qual o comprimento da reta B em cm: '))
reta_c = float(input('Qual o comprimento da reta C em cm: '))

# Mostrar se é possível a existencia de um triângulo

if reta_a < reta_b + reta_c and reta_b < reta_a + reta_c and reta_c < reta_a + reta_b:
    print('O triângulo pode existir!')
else:
    print('Não é possível que esse triânguio exista!')