# Fazer uma progama que pergunte a distânsia de uma viagem em km.
# Sendo o preço da passagem, 0,50$ por km e 0,45$ para viagens acima de 200km

# Pedi adistância da viagem
distancia = float(input('Digite em km a distância da viagem: '))

# Mostre o valor da viagem
if distancia <= 200:
    print(f'Sua viagem ficou {distancia * 0.50}$.')
else:
    print(f'Sua viagem ficou {distancia * 0.45}$.')