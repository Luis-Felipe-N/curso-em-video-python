from datetime import date

# FAZER UM PROGAMA QUE LEIA O NOME, ANO DE NASCIMETO, E A CARTEIRA DE TRABALHO DE UMA PESSOA
# CADASTRE A IDADE DA PESSOA
# SE O CTPS FOR != DE 0, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO 
# CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR
# LEVANDO EM CONTA QUE A PESSOA SE APOSENTA DEPOIS DE 35 ANOS DE CONTRIBUIÇÃO

dados_cadastrais = dict()
ano_atual  = date.today().year

print('-' * 50)
print(f'|{"CADASTRAMENTO DE PESSOAS":^48}|')
print('-' * 50)

dados_cadastrais['nome'] = str(input('Nome: ')).strip().capitalize()# PEGANDO O NOME
ano_de_nascimento = int(input('Ano de nascimento: '))# PEGANDO ANO DE NASIMENTO
dados_cadastrais['idade'] = ano_atual - ano_de_nascimento# CALCULANDO A IDADE COM REFERENCIA COM O ANO DA MAQUINA
dados_cadastrais['ctps'] = int(input('Carteira de trabalho (0 não tem): '))# PEGANDO A CARTEIRA DE TRABALHO, SE FOR 0 NÃO EXECULTA OS DE BAIXO

if dados_cadastrais['ctps'] > 0:
    dados_cadastrais['contratacao'] = int(input('Ano de contratação: '))# PEGANDO ANO DE CONTRATAÇÃO
    dados_cadastrais['salario'] = float(input('Salário: '))# PEGANDO SALARIO
    dados_cadastrais['aposentadoria'] = dados_cadastrais['idade'] + ((35 + dados_cadastrais['contratacao']) - ano_atual)# CALCULANDO A APOSENTADORIA

for chave, valor in dados_cadastrais.items():# MOSTRANDO RESULTADO
    print(f'{chave} = {valor}')