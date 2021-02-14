# Pedi um número de 0 a 9999 e mostrar sua unidade, dezena, centenae minhar milhar

n = input('Digite um número de 0 a 9999: ')
quantidade = len(n)

# mostrar a unidade
if quantidade >= 1:
    print(f'Unidade:{n[-1]}')

# mostar a dezena
if quantidade >= 2:
    print(f'Dezena:{n[-2]}')

# mostar a centena
if quantidade >= 3:
    print(f'Centena:{n[-3]}')

# mostar o milhar 
if quantidade >= 4:
    print(f'Milhar:{n[-4]}')
