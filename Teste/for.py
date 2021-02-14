from time import sleep
i = int(input('inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for i in range(i,f+1,p):
    sleep(1)
    print(i)  
