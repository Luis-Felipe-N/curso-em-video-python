lanches = ('hambúrguer', 'suco', 'refri', 'pudim')
print(lanches[2])# VAI MOSTRAR O REFRI, POIS EM PYTHON SE COMEÇA COM 0
print(lanches[0])# VAI MOSTRAR O HAMBÚRGUER
print(lanches[::])# O PRIMEIRO TERMO É O ÍNDECE/ O SEGUNDO É ATÉ ONDE VAI/ O TERCEIRO É DE QUANTAS CASAS VAI PULAR
print(lanches[:2:2])# COMEÇA DO PRIMEIRO TERMO, VAI ATÉ O TERCEIRO E VAI PULANDO 2 CASAS
print(lanches[-1])# VAI PEGAR O ULTIMO TERMO
print(lanches[-2:])# VAI COMEÇAR DO PENÚLTIMO TERMO ATÉ O ULTIMO
print(lanches[-4::2])# VAI COMEÇAR DO PRIMEIRO TERMO, ATÉ O ULTIMO, PULANDO 2 CASA

# NÃO É POSSIVÉL TROCAR UM TERMO DE UMA TUPLA
# AS TUPLAS  SÃO IMUTÁVEIS
# SE TENTARMOS TROCAR O VALOR VAI  ( lanches[3] = 'sorvete' ) DAR ERRO 


# ORDENANDO TUPLAS EM ORDEM ALFABETICA
print(sorted(lanches))# VAI ORDENAR OS CONTEÚDOS DA TUPLA


# JUNTANDO TUPLAS
a = 4, 3, 3, 2
b = 8, 6, 0, 7
c = a + b
print(c)# O c VAI VIRAR A SOMA DAS TUPLAS


# DELETANDO TUPLAS
del(c)# AS TUPLAS SÃO IMUTAVEIS, MAS PODEMOS DELETAR ELAS
print(c)
