# DIFERENTE DAS TUPLAS AS LISTA SÃO MUTÁVEIS
# ENTÃO EU POSSO A QUALQUER HORA TROCAR UM ITEM QUE ESTÁ DENTRO DELA
# AS LISTA SÃO REPRESENTADAS POR COLCHETES

lanches = ['suco', 'hambúguer','biscoito', 'cachorro-quente']
# QUERO SAIR DA 'DIETA' E TOMAR UM REFRI EM VEZ DO SUCO
lanches[0] = 'refri'
#print(lanches) # ['refri', 'hambúguer', 'biscoito', 'cachorro-quente'] O RESULTADO
# NOTA-SE QUE 'suco' SUMIU

# E SE EU QUISER SÓ ADICIONAR ALGO?
# COM AS LISTA TAMBÉM POSSO ADICIONAR ALGUMA COISA SEM PRECISAR TIRAR OUTRA
# COM O MÉTODO DA LISTA: append('...')
lanches.append('pudim')
#print(lanches) # ['refri', 'hambúguer', 'biscoito', 'cachorro-quente', 'pudim'] O RESULTADO
# NOTA-SE QUE O PUDIM É O ULTIMO DA LISTA

# COMO FAÇO PARA COLOCAR UM YOGURT NO MEIO DA LISTA POR EXEMPLO 
# COM OUTRO MÉTODO DA LISTA: O insert('posição','...')
lanches.insert(3,'yogurt')
#print(lanches) # ['refri', 'hambúguer', 'biscoito', 'yogurt', 'cachorro-quente', 'pudim'] O RESULTADO


lanches.insert(-1,'pastel') # COM O ÍNDICE PODEMOS COLOCAR NA ULTIMA POSIÇÃO, MAS ELA FICOU COMO O PENÚLTIMO
#print(lanches) # ['refri', 'hambúguer', 'biscoito', 'yogurt', 'cachorro-quente', 'pastel', 'pudim']

# SE COLOCARMOS UM NÚMERO MAIOR QUE O DA LISTA, O 'cuscuz' TAMBÉM VAI PARA O ULTIMO LUGAR
lanches.insert(100,'cuscuz') #['refri', 'hambúguer', 'biscoito', 'yogurt', 'cachorro-quente', 'pastel', 'pudim', 'cuscuz']
#print(lanches)

# AAAAA NÃO QUERO MAIS 'cuscuz'
# PODEMOS APAGAR ALGO DA LISTA COM:

del lanches[-1] # ESSE COMANDO SE ULTILIZA O ÍNDICE | VAI APAGAR O ÚLTIMO ITEM DA LISTA
#print(lanches) # ['refri', 'hambúguer', 'biscoito', 'yogurt', 'cachorro-quente', 'pastel', 'pudim']

lanches.pop() # POR PADRÃO ESSE MÉTODO APAGA O ÚLTIMO ITEM, MAS PODEMOS PASSAR UM ÍNDICE
#print(lanches) # ['refri', 'hambúguer', 'biscoito', 'yogurt', 'cachorro-quente', 'pastel']

lanches.remove('hambúguer') # COM O MÉTODO REMOVE VAMOS PASSAR O QUE QUEREMOS APAGAR
#print(lanches) # ['refri', 'biscoito', 'yogurt', 'cachorro-quente', 'pastel']

# TODOS OS MÉTODO E FUNÇÃO REVOME TAMBÉM O ÍNDICE 

# CRIANDO LISTA COM RANGE()
valores = list(range(9,17)) # O RANGE JÁ CRIA UMA LISTA DE FORMA ORDENADA, SE VOCÊ CONHECE  ESTRUTURA DE REPETIÇÃO ESTÁ BEM FAMILIARIZADO
print(valores) # [9, 10, 11, 12, 13, 14, 15, 16]

# SE TIVER UMA LISTA DESORDENADA E QUISER ORDENAR 
# USA A FUNÇÃO SORT
valores1 = [6,8,2,9,7,1,5,4,3] 
valores1.sort()
print(valores1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]