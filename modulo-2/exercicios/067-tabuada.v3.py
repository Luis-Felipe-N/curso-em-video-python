while True:
    print('-=' * 14)
    tabuada = int(input('Quer ver a taabuada de que: '))
    print('-=' * 14)
    if tabuada < 0:
        break
    for x in range(0,11):
        print(f'{tabuada} x {x} = {tabuada * x}')
print('FIM')