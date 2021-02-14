from math import radians, sin, cos, tan
# Pedi o um ângulo e mostrar seno, coseno, e tangente.
# 1 pedi o ângulo
# 1 calcular o seno, cosseno, tangente
# 1 mostrar resultado
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de {} é {:.2f}.'.format(angulo, seno))
print('o cosseno de {} é {:.2f}.'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}.'.format(angulo, tangente))