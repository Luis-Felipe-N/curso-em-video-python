from math import hypot
#Calcular a hipotenusa de um trinagulo retangulo
# 1 pedi o comprimento do cateto oposto
# 2 pedi o comprimento docateto adjacente 
# 3 calcular a hipotenusa que é : a² = c² + b². Onde pode '²' ser 1/2
 
co = float(input('Digite o comprimeto do cateto oposto: '))
ca = float(input('Digite o comprimteto do cateto adjacente: '))
hipotenusa =  hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hipotenusa))