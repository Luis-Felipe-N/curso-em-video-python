lanches = 'hambúrguer', 'suco', 'refri', 'sorvete'

# COM FOR PODEMOS IMPRIMIR TODOS ELEMENTOS SEPARADAMENTE, JÁ QUE ELE ACEITA O range() OU UMA VARÍAVEL
for comida in lanches:
    print(f'Eu comi {comida}.')

# COMO PODEMOS FATIAR AS TUPLAS, HÁ OUTRA MANEIRA DE MOSTRAR OS ELEMENTOS
for c in range(len(lanches)):# O LEN RETORNA A QUANTIDADE DE TERMOS DA TUPLAS
    print(f'O {lanches[c]} ESTÁ NA POSIÇÃO {c}')# POSSIBILITANDO TAMBÉM MOSTRAR SUA POSIÇÃO

for pos, comida in enumerate(lanches):# O ENUMERATE TAMBÉM RETORNA A POSIÇÃO PARA O pos ENQUANTO O lanches RETORNA PARA comida
    print(f'O {comida} ESTÁ NA POSIÇÃO {pos}')