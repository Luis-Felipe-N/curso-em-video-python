# Fazer um progama que leia duas notas e mostre:
# Média abaixo de 5.0 - REPROVADO
# Média entre 5.0 de 6.9 - RECUPERAÇÃO
# Média 7.0 ou superior - APROVADO

# Pedindo as notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média é de {:.2f}.\nVocê está \033[31mREPROVADO\033[m'.format(media))
elif media < 6.9:
    print('Sua média é de {:.2f}.\nVocê está de \033[33mRECUPERAÇÃO\033[m'.format(media))
elif media > 7:
    print('Sua média é de {:.2f}.\nVocê está \033[32mAPROVADO\033[m'.format(media))