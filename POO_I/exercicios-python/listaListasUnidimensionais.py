# LISTA - LISTAS UNIDIMENSIONAIS

def maxLista(lista):
    max = -10000
    for el in lista:
        if int(el) > int(max):
            max = el
    return max

def minLista(lista):
    min = 10000
    for el in lista:
        if int(el) < min:
            min = el
    return min

def multiple(num, m):
    if num % m == 0:
        return True
    else:
        return False

# MAIN

n = int(input('Digite o número de suspeitos: '))
while n != 0:
    suspeitos = input('Digite, separado com um espaço, o quanto suspeito são essas n pessoas: ').split(' ')
    aux = list(suspeitos)
    aux.remove(maxLista(suspeitos))
    print(maxLista(aux))
    print(f'O culpado é o suspeito com índice: {suspeitos.index(maxLista(aux)) + 1}')
    n = int(input('\nDigite o número de suspeitos: '))

n = int(input('Digite a quantidade de números: '))
nums = [int(nums) for nums in input('Digite os números separados por um espaço: ').split()]

m2 = 0
m3 = 0
m4 = 0
m5 = 0
for num in nums:
    if multiple(num, 2):
        m2 += 1
    if multiple(num, 3):
        m3 += 1
    if multiple(num, 4):
        m4 += 1
    if multiple(num, 5):
        m5 += 1

print(f'{m2} Múltiplo(s) de 2 \n{m3} Múltiplo(s) de 3 \n{m4} Múltiplo(s) de 4 \n{m5} Múltiplo(s) de 5')

n = int(input('Digite N: '))
seq = [int(seq) for seq in input('Digite a sequência separando os números com um espaço: ').split()]
seq = set(seq)
seqFull = set()
for i in range(n, 0, -1):
    seqFull.add(i)

print(f'Na sequência digitada está faltando o(s) número(s): {seqFull.difference(seq)}')