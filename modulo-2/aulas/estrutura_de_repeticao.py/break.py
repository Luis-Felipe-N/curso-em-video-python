cont = s = 0
while True:# ISSO É UM LOOP INFINITO, QUE NUNCA ACABA
    n = int(input('Numero [999 para parar]: '))
    if n == 999:
        break # SÓ COM O BREAK PODEMOS PARAR UM LOOP INFINITO | ASSIM QUANDO O USUÁRIO DIGITAR 999 O NUMERO NÃO VAI PARA O s
    s += n
print(s)