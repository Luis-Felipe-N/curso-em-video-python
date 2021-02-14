'''Como no desafil 035 vamos ler três retas, e além de mostrar a existencia de um triangulo
   Mostrar se o tipo dos triangulos.
   - Equilátero: todos os lados iguais
   - Isósceles: dois lados iguais
   - Escaleno :todos lados diferentes'''

reta1 = float(input('Qual o comprimento da primeira reta: '))
reta2 = float(input('Qual o comprimento da segunda reta: '))
reta3 = float(input('Qual o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    if reta1 == reta2 == reta3:
        print('Pode existir um triâgulo Equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Pode existir um triângulo Isósceles.')
    else:
        print('Pode existir um triâgulo Ecaleno')
else:
    print('Não piode existir um triângulo')