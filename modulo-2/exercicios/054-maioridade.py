from datetime import date
# FAZER UM PROGAMA QUE LEIA 7 IDADES E MOSTRE QUANTOS SÃO MAIOR DE IDADE E QUANTOS AINDA NÃO SÃO
# CONSIDERANDO A MAIORIDADE 21 ANOS

# CRIANDO ALGUMAS VARIÁVEIS QUE VAMOS ULTILIZAR
lista_maior_de_idade = []

# PEGANDO OS ANOS DE NASCIMENTO
for c in range(1, 8):
    ano_de_nascimento = int(input(f'EM QUE ANO A {c}ª NASCEU: '))
    if date.today().year - ano_de_nascimento >= 21:
        lista_maior_de_idade.append(ano_de_nascimento)
print(f'DAS 7 IDADES TEMOS {len(lista_maior_de_idade)} MAIOR DE IDADE E {7 - len(lista_maior_de_idade)} MENOR DE IDADE.')
