# Fazer um progama que leia a altura e o peso da pessoa e mostre seu IMC
# Formula para calcular o IMC  - IMC = Peso ÷ (Altura × Altura)

'''
-Abaixo de 18.5 : Abaixo do peso
-Entre 18.5 e 25 : Peso ideal
-25 até 30 : Sobrepeso
-30 a 40 : Obesidade
-Acima de 40:Obesidade mórbida
'''

# Pegando o peso e autura
peso = float(input('Seu peso em kilo gramas: '))
altura = float(input('Sua altura em metros: '))



# Calculando IMC
imc = peso / (altura * altura)
print('Seu IMC é {:.1f}.'.format(imc))
#=======
if imc < 18.5:
    print('\033[36mVocê está abaixo do peso.\033[m')
elif imc < 25:
    print('\033[32mVocê está no peso ideal.\033[m')
elif imc < 30:
    print('\033[33mVocê está com sobrepeso.\033[m')
elif imc <= 40:
    print('\033[31mVocê etsá Obeso.\033[m')
elif imc > 40:
    print('\033[40mObesidade mórbida\033[m')
    