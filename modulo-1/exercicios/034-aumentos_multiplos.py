# Fazer um progqama que peça o salário de uma pessoa e aumente:
# 10% para salários superiores a 1.250,00$
# 15% para salários inferiores

# Pedir o salário
salario = float(input('Me informe seu salário:R$ '))

# Calcular o reajuste
reajuste_10 = salario * 10 / 100
reajuste_15 = salario * 15 / 100

# Mostra o reajuste deacorddo com seu salários
if salario >= 1250:
    print(f'Seu salário vai ficar {salario + reajuste_10}.')
else:
    print(f'Seu salário vai ficar {salario + reajuste_15}.')