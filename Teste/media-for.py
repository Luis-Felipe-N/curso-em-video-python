s = 0
n = 0
for c in range(0,4):
    n += 1
    v = float(input('Nota{}: '.format(n)))
    s += v
print('A média é {}'.format(s / 4))