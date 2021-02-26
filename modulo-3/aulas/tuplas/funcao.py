# COMO TRABALHAMOS MUITO COM ROTINAS, CRIAR UMA FUNÇÃO E CHAMA-LA NO CÓDIGO FACILITA MUITO NÃO TER QUE ESCREVER A MESMA LINHA VÁRIAS VEZES
# USAMOS O COMANDO DEF PARA DECLARAR UMA FUNCAO, DEPOIS UM NOME PARA A FUNÇÃO EX:

# def nomeDaFuncao():
#     # BLOCO COM O CÓDIGO QUE DESEJA QUE SEJÁ EXECULTADO NA CHAMADA DA FUNÇÃO
#     print('Funcionando')


# nomeDaFuncao()# O RESULTADO FUI ("Funcionando")




# SEMPRE QUE PRESCISAMOS MOSTRAR UMA LINHA ESCREVEMOS TODA VEZ O MESMO CÓDIGO
# PARA FACILITAR PODEMOS CRIAR UMA FUNÇÃO QUE MOSTRE ESSA LINHA SEM PRESCISAR ESCREVER O CÓDIGO PRINT VÁRIAS VEZES

def caixa(tipo, msg):
    print(tipo * (len(msg) * 2))
    print(msg)
    print(tipo * (len(msg) * 2))


caixa('#', 'Python')# O RESULTADO É
'''
############
Python
############'''

# MAS PODE VARIAER DE ACORDO COM O TEXTO SOLICITADO




def soma(a, b):# DOIS PARAMENTROS a E b QUE SEMPRE QUANDO A FUNÇÃO FOR CHAMADA DEVE INSIRIR ESSES DOIS VALORES
    s = a + b
    print(s)


soma(1, 4)# RESULTADO É 5
soma(b=3, a=1)# RESULTADO É 4, RECLARAMOS QUE O B=3 E A=1 




def contador(*n):# O PARAMETRO AGORA PODE RECEBER VÁRIOS VALORES, QUANDDO COLOCAMOS O * O PYTHON SABE QUE VAI RECEBER VALORES VARIADOS
    # TODOS OS VALORES VÃO SER GUARDADO DENTRO DE UMA TUPLA
    print(len(n))


contador(1, 5, 7, 7)



def dobrar(list):
    p = 0
    while p < len(list):
        list[p] *= 2
        p += 1 
    valoresd = list[:]
    return valoresd

valores = [1, 2, 9, 7, 4]
print(valores)
dobrar(valores)
print(valores)
