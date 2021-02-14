# FAZER UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E UMA RAZÃO DE UMA PROGRESSÃO ARITMÉTICA
# MOSTRAR OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITMÉTICA

termo_p = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
decimo = termo_p + (10 - 1) * razao

for c in range(termo_p, decimo + razao, razao):
    print(c, '-> ', end='')
print('ACABOU!')