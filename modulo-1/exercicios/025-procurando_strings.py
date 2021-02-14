# ler um nome e verificar se há Silva no nome

#1-pedi o nome completo
nome_completo = input('Digite seu nome completo: ')

#2-colocar o nome em uma sintaxe universal
nome_completo = nome_completo.upper()

#3-pegar o True ou False da variável/ com o 'i' é possivel analisar se há algo na váriavel
tem_silva = 'SILVA' in nome_completo

#4-mostra para o usuário se tem ou não o silva
if tem_silva == True:
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva!')