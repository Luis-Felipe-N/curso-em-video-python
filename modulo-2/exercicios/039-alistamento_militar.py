from datetime import date
# Fazer um progama que leia a idade de uma pesso e mostre:
# Se ele já se alistou, tem que se alistar ou quando vai se alistar.

# Pegando a idade
ano_nascimento = int(input('Em que ano você nasceu: '))
genero = int(input('qual seu gênero?\n[1] - HOMEN\n[2] - MULHER\nQual seu gênero: '))

# Ano atual
ano = date.today().year
idade = ano - ano_nascimento

# Mostrando se pode ou não se alistar
if genero == 2:
    print('Sorte sua, mulher não pode se alistar.')
elif idade < 18:    
    print('Você só tem {} anos só pode se alistar {}.'.format(idade, ano + (18 - idade)))
    print('Ainda falta {} anos para voê se alistar.'.format(18 - idade))
elif idade > 18:
    print('Você tem anos {}.'.format(idade))
    print('Você já de se alisto em {}.'.format(ano - (idade - 18)))
    print('Você deveria se alistar há {} anos atrás.'.format(idade - 18))
else:
    print('Você tem 18 anos.')
    print('Se aliste \033[31mIMEDIATAMENTE!\033[m')