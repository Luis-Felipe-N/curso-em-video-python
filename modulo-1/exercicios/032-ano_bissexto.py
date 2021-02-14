from datetime import date
# Fazer um progama que peça um ano qualquer e mostre se ele é um ano bissexto
# Os anos bissexto se o ano não terminar em 00 ée for divisivel por 4 ele é um ano bissexto


# Pedi o ano
ano = int(input('digite o ano que desejar ou 0 para o ano atual: '))

# Calcular se é 
if ano == 0:
    ano = date.today().year

ano_bissexto11 = ano % 4
ano_bissexto_00 = ano % 400

# Mostrar se o ano é ano é bissexto ou não
if ano_bissexto_00 == 0 or ano_bissexto11 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
