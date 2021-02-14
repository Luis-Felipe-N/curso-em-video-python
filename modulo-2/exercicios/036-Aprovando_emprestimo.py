# Uma pessoa que fazer uma empréstimo bancário para a compra de uma casa.
# Ela dá o valor da casa, o seu salário e em quantos anos ela vai pagar
# O calculo para ver se essa pessoa pode fazer esse empréstimo é o seguinte:
# pegar o valor da casa descobrir em quantas parcelas e o valor sabendo que o valor da parcela não pode excede 30% do salário da pessoa 

# Pegando os dados da cliente
valor_casa = float(input('Qual será o valor da casa: R$'))
valor_salario = float(input('Quanto voçê recebe: R$'))
prestacao = int(input('Em quantos anos voçê deseja quitar a prestação: '))



# Analisando se a pessoa pode fazer o empréstimo
valor_prestacao = valor_casa / (prestacao * 12)
minimo = valor_salario * 30 / 100

print('O valor da prestação será {:.2f} em {} meses.'.format(valor_prestacao, prestacao * 12))

if valor_prestacao <= minimo:
    print(f'\033[32mEmprésrtimo aprovado!\033[m')
else:
    print(f'\033[31mEmpréstimo negado!\033[m')


