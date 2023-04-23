# EXERCÍCIOS DE LISTA E TUPLA

def validarNota(n):
    if n >=0 and n <= 10:
        return n
    else:
        return validarNota(int(input('Nota inválida [0, 10]. Digite novamente: ')))
    
def mudarValores(lista):
    aux = []
    for i in range(0, len(lista)):
        aux.append(lista[len(lista)-1-i])
    return aux

def somarLista(lista):
    sum = 0
    for el in lista:
        sum += el
    return sum

def maxLista(lista):
    max = -10000
    for el in lista:
        if el > max:
            max = el
    return max

def minLista(lista):
    min = 10000
    for el in lista:
        if el < min:
            min = el
    return min

def multiplyK(lista, K):
    aux = []
    for el in lista:
        aux.append(el*K)
    return aux
    
# MAIN

for i in range(1, int(input('Digite o número de alunos: '))+1):
    notas = []
    maior = -1
    menor = 11
    nome = input(f'Digite o nome do {i} aluno(a): ')
    for j in range(1, 4):
        n = validarNota(int(input(f'Digite a {j}º nota de {nome}: ')))
        notas.append(n)
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print(f'Média de {nome} = {float(somarLista(notas)/len(notas)):.2f}\n')
    print(f'Maior nota de {nome}: {maior}')
    print(f'Menor nota de {nome}: {menor}\n')

n = []
for i in range(0, int(input('Digite o número de elementos da lista: '))):
    n.append(int(input(f'Valor n[{i}]: ')))
    
aux = False
for el in n:
    if n.count(el) > 1:
        aux = True
        break

if aux:
    print('Há elementos repetidos!')
else:
    print('Não há elementos repetidos!')
    
tupla = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(f'Maior elemento: tupla[{tupla.index(maxLista(tupla))}]')
print(f'Menor elemento: tupla[{tupla.index(minLista(tupla))}]')

n = []
for i in range(0, int(input('Digite o número de elementos da lista: '))):
    n.append(int(input(f'Valor n[{i}]: ')))

K = int(input('Digite o valor de K: '))
n = multiplyK(n, K)
print(n)

X = []
print('Digite os valores da lista abaixo em sequência: ')
for i in range(0, 20):
    X.append(int(input('')))

X = mudarValores(X)
print(X)

atleta = input('Nome do atleta: ').upper()
while atleta != 'O':
    saltos = []
    for i in range(1, 6):
        saltos.append(float(input(f'{i}º salto: ')))
    maior = maxLista(saltos)
    menor = minLista(saltos)
    saltos.remove(maior)
    saltos.remove(menor)
    media = somarLista(saltos)/len(saltos)

    print(f'\nMelhor salto: {maior:.2f} m')
    print(f'Pior salto: {menor:.2f} m')
    print(f'Média dos saltos restantes: {media:.2f} m\n')

    atleta = input('Nome do atleta: ').upper()