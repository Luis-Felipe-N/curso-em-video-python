# NÃO TEM MUITO O QUE FALAR, NOSSO CÓDIGO SEMPRE TEM ALGUMAS EXEÇÕES
# EXEMPLO: ESTAMOS ESPERANDO UM NÚMERO INTEIRO E O USUÁRIO INSIRE UM NÚMERO REAL, ISSO É UMA EXEÇÃO, POIS NO NOSSO CÓDIGO NÃO TEM NENHUM ERRO

# a = int(input('digite um número inteiro: '))# SE O USUÁRIO COLOCAR QUALQUER COISA QUE NÃO SEJA UM NÚMERO INTEIRO VAI DÁ : ValueError

# PARA NÃO DÁ MAIS ERROS USAMOS O COMADDO TRY

# try:
#     a = int(input('digite um número inteiro: '))
# except:
#     print('\033[31mDeu um erro inesperado!\033[m')
#     # SE DER ERRO MOSTRE 'DEU ERRRO...'


# try:
#     a = int(input('digite um número inteiro: '))
# except:
#     print('\033[31mDeu um erro inesperado!\033[m')
#     # SE DER ERRO MOSTRE 'DEU ERRRO...'
# else:
#     print(f'\033[32mDeu certo o resultado é {a}\033[mn')


# O COMANDO FINALLY SERÁ EXECULTADO SEMPRE, NÃO IMPORTA SE DER ERRO OU NÃO


# try:
#     a = int(input('digite um número inteiro: '))
# except:
#     print('\033[31mDeu um erro inesperado!\033[m')
#     # SE DER ERRO MOSTRE 'DEU ERRRO...'
# else:
#     print(f'Você digitou o número {a}!')
# finally:
#     print(f'\033[32mFim do progama!\033[m')
#     # SUPONDO QUE O USUÁRIO INSIRIO 3, O RESULTAO SERÁ: 
# # Você digitou o número 4!  
# # Fim do progama!


# PODEMOS MOSTRAR UMA MENSAGEM PERSONALIZADA COM A CLASS DO ERRO

# try:
#     a = int(input('Digite um número inteiro: '))
# except Exception as erro: # CRIAMOS UMA VARIÁVEL PARA O ERRO
#     print(f'O ocorreu um erro da clase {erro.__class__}')# O ocorreu um erro da clase <class 'ValueError'>
#     # ESSE ERRO OCORREU PELOMFATO DE EU DIGITAR 'oi'

