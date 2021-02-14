# Pedi para o usuário digitar uma frase e mostrar:
frase = str(input('Digite uma frase: ')).strip()
frase = frase.lower()

# Quantas vezes aparece o A
print(f'A na frase tem {frase.count("a")} as.')

# Em que posição o A aparece na primeira vez
print(f'O primeiro A aparece na posição {frase.find("a") + 1}.')

# Em que posição o A aparece pela ultima vez
print(f'O ultimo A aparece na posição {frase.rfind("a") + 1}.')