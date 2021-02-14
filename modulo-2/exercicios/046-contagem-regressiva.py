from time import sleep
import emoji

# FAZER UM PROGAMA QUE FAÇA UMA CONTAGEM REGRESIVA DE 10 A 0

for c in range(10, -1, -1):
    print('\033[{}m{}\033[m'.format(30 + c, c))
    sleep(1)
print((emoji.emojize('FELIZ ANO! :fireworks:')))