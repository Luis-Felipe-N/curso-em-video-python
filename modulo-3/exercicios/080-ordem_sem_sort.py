# FAZER UM PROGAMA QUE LEIA 5 NÚMEROS E COLOQUE EM ORDEM SEM SOR
nums = list()

for n in range(0,5):
    num = int(input('Digite um valor: '))# PEGNADO O VALOR
    
    if n == 0:
        nums.append(num)
        print('Número aicionado na útima posição...')
    if n == 1:
        if num > max(nums):
            nums.append(num)
            print('Número aicionado na útima posição...')
        else:
            nums.insert(0, num)
            print('Número aicionado na posição 0...')
    if n == 2:
        if num > max(nums):
            nums.append(num)
            print('Número aicionado na útima posição...')
        elif num > min(nums) and num < max(nums):
            nums.insert(1, num)
            print('Número aicionado na posição 1...')
        else:
            nums.insert(0, num)
            print('Número aicionado na posição 0...')
    if n == 3:
        if num > max(nums):
            nums.append(num)
            print('Número aicionado na útima posição...')
        elif num > min(nums[1:]) and num < max(nums):
            nums.insert(2, num)
            print('Número aicionado na posição 2...')
        elif num > min(nums) and num < max(nums):
            nums.insert(1, num)
            print('Número aicionado na posição 1...')
        else:
            nums.insert(0, num)
            print('Número aicionado na posição 0...')
    if n == 4:
        if num > max(nums):
            nums.append(num)
            print('Número aicionado na útima posição...')
        elif num > min(nums[2:]) and num < max(nums):
            nums.insert(3, num)
            print('Número aicionado na posição 3...')
        elif num > min(nums[1:]) and num < max(nums):
            nums.insert(2, num)
            print('Número aicionado na posição 2...')
        elif num > min(nums) and num < max(nums):
            nums.insert(1, num)
            print('Número aicionado na posição 1...')
        else:
            nums.insert(0, num)
            print('Número aicionado na posição 0...')
print(nums)