from datetime import date
# Deacordo com a idade classifique se o atleta é:
# Até 9 anos = MIRIN
# Até 14 anos = INFANTIL
# Até 19 anos = JUNIOR
# Até 20 anos = SÊNIOR
# Acima = MASTER

print('\033[32mAea Atleta!\033[m')

# Pedindio a idade
nascimento = int(input('EM que ano você nasceu: '))
idade = date.today().year - nascimento

# Classificando
if idade <= 9:
    print(f'Você tem {idade} anos. Você é um atleta \033[32mMIRIN\033[m.')
elif idade <= 14:
    print(f'Você tem {idade} anos. Você é um atleta \033[36mINFANTIL\033[m.')
elif idade <= 19:
    print(f'Você tem {idade} anos. Você é um atleta \033[34mJUNIOR\033[m.')
elif idade <= 20:
    print(f'Você tem {idade} anos. Você é um atleta \033[35mSÊNIOR\033[m.')
else:
    print(f'Você tem {idade} anos. Você é um atleta \033[31mMASTER\033[m.')