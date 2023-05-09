# LISTA DE EXERCÍCIOS: LISTA COMPOSTA

import random
import math

def maxLista(lista):
    max = None
    for el in lista:
        if max == None:
            max = el
        elif el > max:
            max = el
    return max

def minLista(lista):
    min = None
    for el in lista:
        if min == None:
            min = el
        elif el < min:
            min = el
    return min

def sort(lista):
    aux = list(lista)
    sort = lista[:]
    for i in range(0, len(aux)):
        sort[i] = minLista(aux)
        aux.remove(sort[i])
    return sort
        
def inverteLista(lista):
    aux = lista[:]
    i = len(aux) -1
    for el in lista:
        aux[i] = el
        i -= 1
    return list(aux)

def ordenarPessoasPeso(pessoas):
    pessoas = list(pessoas)
    pesos = []
    for pessoa in pessoas:
        pesos.append(pessoa[2])
    pesos = list(sort(pesos))
    sorted = []
    for peso in pesos:
        for pessoa in pessoas:
            if pessoa[2] == peso:
                sorted.append(pessoa)
                pessoas.remove(pessoa)
    aux = []
    for el in sorted:
        aux.append(el[0])
    return aux

def ordenarIdadeMaiorQue(pessoas, age):
    pessoas = list(pessoas)
    sorted = []
    for pessoa in pessoas:
        if pessoa[1] > age:
            sorted.append(pessoa)
    for pessoa in sorted:
        pessoa.pop(2)
    return sorted

def somaLinhaMatriz(matriz, linha):
    sum = 0
    for el in matriz[linha]:
        sum += el
    return sum

def printarMatrizEstilizada(matriz):
    for linha in matriz:
        print(f'{linha}')

def somarElementosAbaixoDiagonal(matriz):
    sum = 0
    for i, linha in enumerate(matriz):
        for j, coluna in enumerate(linha):
            if j < i:
                sum += coluna
    return sum

def todosProblemas(matriz, M, N):
    for i in range(0, N):
        verif = True
        for j in range(0, M):
            if matriz[i][j] != "1":
                verif = False
                break
        if verif:
            return True
    
    return False

def problemaResolvidoPorTodos(matriz, M, N):
    for i in range(0, M):
        verif = True
        for j in range(0, N):
            if matriz[i][j] != "1":
                verif = False
                break
        if verif:
            return True
    
    return False

pessoas = []
while True:
    pessoa = [input('Digite o nome da pessoa: '), int(input('Digite a idade da pessoa: ')), float(input('Digite o peso da pessoa: '))]
    pessoas.append(pessoa[:])
    if input('Deseja adicionar uma nova pessoa [S/N]: ').upper() == 'N':
        print(f'------------------------------------------------------\n')
        break

print(f'Foram cadastradas {len(pessoas)} pessoa(s). \nPessoas mais pesadas: {inverteLista(ordenarPessoasPeso(pessoas))}. \nPessoas mais leves: {ordenarPessoasPeso(pessoas)}. \nPessoas com mais de 20 anos: {ordenarIdadeMaiorQue(pessoas, 20)}')

n = int(input('Digite a linha a ser operada na matriz: '))
op = input('Digite o caractere da operação a ser realizada [S/M]: ')
l = int(input('Digite a ordem da matriz: '))
ran = input('Preencher randômicamente [S/N]: ')
M = []
for lin in range(0, l):
    linha = []
    for col in range(0, l):
        if ran.upper() == "N":
            linha.append(int(input(f'Digite M[{lin}][{col}]: ')))
        else:
            linha.append(random.randint(0, 99))
    M.append(linha[:])
    linha.clear()

printarMatrizEstilizada(M)
if op.upper() == "S":
    print(f'\n\n\nSoma da linha {n} da matriz M = {somaLinhaMatriz(M, n)}\n\n\n')
else:
    print(f'\n\n\nMédia da linha {n} da matriz M = {(somaLinhaMatriz(M, n)/l):.2f} \n\n\n')
printarMatrizEstilizada(M)

op = input('Digite o caractere da operação a ser realizada [S/M]: ')
l = int(input('Digite a ordem da matriz: '))
ran = input('Preencher randômicamente [S/N]: ')
M = []
for lin in range(0, l):
    linha = []
    for col in range(0, l):
        if ran.upper() == "N":
            linha.append(int(input(f'Digite M[{lin}][{col}]: ')))
        else:
            linha.append(random.randint(0, 99))
    M.append(linha[:])
    linha.clear()

printarMatrizEstilizada(M)
if op.upper() == "S":
    print(f'\n\n\nSoma da parte inferior da diagonal principal da matriz M = {somarElementosAbaixoDiagonal(M)}\n\n\n')
else:
    print(f'\n\n\nMédia da parte inferior da diagonal principal da matriz M = {(somarElementosAbaixoDiagonal(M)/l):.2f} \n\n\n')
printarMatrizEstilizada(M)

N, M = input('Digite separado por um espaço N e M: ').split(' ')
N = int(N)
M = int(M)
while N != 0 and M != 0:
    matriz = []
    carac = 0

    print('A seguir digite os M números (0 ou 1) nas N linhas: ')
    for i in range(0, N):
        linha = input('').split(' ')
        matriz.append(linha)

    if todosProblemas(matriz, M, N) == False:
        print("Ninguém resolveu todos os problemas.")
        carac += 1

    
    count = 0
    for i in range(0, M):
        for j in range(0, N):
            if matriz[i][j] == "1":
                count += 1
                break
    if count >= 3:
        print("Cada problema foi resolvido por pelo menos uma pessoa (não necessariamente a mesma).")
        carac += 1
    
    if problemaResolvidoPorTodos(matriz, M, N) == False:
        print("Não há problema resolvido por todos.")
        carac += 1
    
    for problemas in matriz:
        if list(problemas).count('1') >= 1:
            verif = True
        else:
            verif = False
            break
    
    if verif:
        print("Todos resolveram pelo menos um problema (não necessariamente o mesmo).")
        carac += 1

    print(f'{carac} Característica(s) Validada(s).\n')

    N, M = input('Digite separado por um espaço N e M: ').split(' ')
    N = int(N)
    M = int(M)

n = int(input('Digita a quantidade de cidadãos que aderiram a pesquisa: '))
pesq = input('Digite separado por um espaço a opinião dos participantes: ').split(' ')
yes = pesq.count('0')
if (yes > math.ceil(n/2) and n % 2 == 0) or (yes >= math.ceil(n/2) and n % 2 != 0):
    print("Y")
else:
    print("N")

n, nVolt = input('Digite separado com um espaço o número de voluntário que foram e quantos voltaram: ').split(' ')
n = int(n)
nVolt = int(nVolt)
voltaram = input('Digite separado com um espaço quais voluntários voltaram: ').split()
if nVolt == n:
    print("*")
else:
    for i in range(1, n+1):
        if voltaram.count(str(i)) == 0:
            print(i, end=" ")
    print("\n")

n, p = input("Digite separado por um espaço o número de canos e a altura do pulo do sapo: ").split(" ")
canos = input("Agora digite separado por um espaço a altura de cada um dos N canos: ").split(" ")

verif = True
for i, cano in enumerate(canos):
    
    if i < int(n)-1:
        if abs(int(cano) - int(canos[i+1])) <= int(p):
            continue
        else:
            verif = False
            break

if verif:
    print("VOCÊ GANHA!")
else:
    print("GAME OVER!")