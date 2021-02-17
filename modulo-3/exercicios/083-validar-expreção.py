exprecao = []
cont_parenteses1 = cont_parenteses2 = 0

exprecao.append(str(input('Expreção: ')))

for e in exprecao[0]:
    if e in '(':
        cont_parenteses1 += 1
    elif e in ')':
        cont_parenteses2 += 1

if cont_parenteses1 == cont_parenteses2:
    print('A expreção está correta!')
else:
    print('A expreção está incorreta!')
