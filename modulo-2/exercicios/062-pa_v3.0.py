# FAZER UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E UMA RAZÃO DE UMA PROGRESSÃO ARITMÉTICA
# MOSTRAR OS 10 PRIMEIROS TERMOS DA PROGRESSÃO ARITMÉTICA

pa = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
n = 0
verificacao = False
vezes = 10
while verificacao == False:
    while n != vezes:
        n += 1
        print(pa , '-> ', end='')
        pa += razao
    print('PAUSA')
    n_vezes = int(input('Mais quantos números: '))
    vezes += n_vezes
    if n_vezes <= 0:
        verificacao = True
print('Forão mostrados {} resultados.'.format(vezes))