# SIMULADO PROVA 1

import math

# FUNÇÃO PERGUNTA 1
def placas(c, d):
    num = math.pow(26, c)*math.pow(10, d)
    return num

# FUNÇÕES PERGUNTA 3
def soma(inicio, fim):
    inicio = int(inicio)
    fim = int(fim)
    soma = 0
    for i in range(inicio, fim+1):
        soma += i
    print(f'Soma [{inicio}, {fim}] = {soma}')

def subtracao(a, b):
    a = int(a)
    b = int(b)
    if a >= b:
        print(f'Subtração: {a-b}')
    else:
        print(f'Subtração: {b-a}')

# FUNÇÕES PERGUNTA 4
def isPrimo(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    
    return True

def encontraPrimos(n):
    if isPrimo(n) == False:
        for i in range (n, 3, -1):
            if isPrimo(i):
                return i
    
    if isPrimo(n):
        return n
        
# MAIN

# PERGUNTA 1
while True:
    c,d = input('Digite o número de consoantes e de dígitos (separado por um espaço): ').split(' ')
    if int(c) == 0 and int(d) == 0:
        print(f'Número de placas possíveis: 0')
    else:
        print(f'Número de placas possíveis: {placas(int(c), int(d))}')
    if input('Deseja continuar? [S/N]: ').upper() == "N":
        break

# PERGUNTA 2
n = int(input('Digite o número total de pessoas: '))
t = 0
intervalo = 0
for i in range(1, n+1):
    p = int(input(f'Digite o tempo em que a {i}ª pessoa passou pelo sensor: '))
    
    if p < intervalo:
        t += 10 - (intervalo - p)
    else:
        t += 10

    intervalo = p + 10

print(f'Tempo total que a escada ficou ligada: {t} segundo(s).')

# PERGUNTA 3
while True:
    inicio, fim = input('Digite o intervalo com um espaço entre os dois valores: ').split(' ')
    a, b = input('Digite os dois valores com um espaço entre eles: ').split(' ')
    soma(inicio, fim)
    subtracao(a, b)
    if input('Deseja continuar? [S/N]: ').upper() == "N":
        break
    
# PERGUNTA 4
cont = int(input('Digite o número de verificações: '))
for i in range(0, cont):
    n, m = input('Digite os valores de N e M separados por um espaço: ').split(' ')
    print(encontraPrimos(int(n))*encontraPrimos(int(m)))

print('Fim')

