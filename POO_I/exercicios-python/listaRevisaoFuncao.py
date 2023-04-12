# LISTA REVISÃO FUNÇÃO
import math

def verificaEntrada01(n):
    if n == "0" or n == "1":
        return int(n)
    else:
        return int(verificaEntrada01(input('Valor inválido! Digite novamente: ')))
    
def calcula_distancia(t, v):
    return t*v

def restricao(x, y):
    if (x > 120 or y > 120) or (x < 1 or y < 0):
        x, y = input('Valores inválidos! Digite x e y novamente separados por um espaço: ').split(' ')
        x, y = restricao(int(x), int(y))
    else:
        return x,y
    
def restricaoPipa(x, y):
    if (x > 100 or y > 100) or (x < 1 or y < 1):
        x, y = input('Valores inválidos! Digite x e y novamente separados por um espaço: ').split(' ')
        x, y = restricao(int(x), int(y))
    else:
        return x,y
    
def restricaoN(n):
    if n >= 2 and n <= 300:
        return int(n)
    else:
        return restricaoN(int(input('Valor inválido! Digite novamente: ')))
    
def calculaAreaPerimetro(x, y):
    a = float((x*y)/2)
    p = float(4*(math.sqrt(math.pow((x/2), 2) + math.pow((y/2), 2))))
    return a, p

def isPrimo(n):
    for i in range (n-1, 1, -1):
        if n % i == 0:
            return False
        
    return True
        
    
# MAIN

while True:
    a = verificaEntrada01(input('Digite o valor escolhido por Alice: '))
    b = verificaEntrada01(input('Digite o valor escolhido por Beto: '))
    c = verificaEntrada01(input('Digite o valor escolhido por Clara: '))

    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a != b and b == c:
            print('Alice ganhou!')
        elif b != a and a == c:
            print('Beto ganhou!')
        elif c != b and b == a:
            print('Clara ganhou!')
        else:
            print('O jogo empatou!')
        print(f'\n')

n = int(input('Digite o número de valores a ser informado: '))
dist = 0
for i in range(0, n):
    t, v = input('Digite os valores de t e v (separados por um espaço): ').split(' ')
    t, v = restricao(int(t), int(v))
    dist += calcula_distancia(t, v)

print(f'Ditância total percorrida de {dist} km, percorrendo os {n} trechos.')

n = int(input('Digite a quantidade de pipas: '))

for i in range(0, n):
    x, y = input('Digite x e y separados por um espaço: ').split(' ')
    x, y = restricaoPipa(int(x), int(y))
    a, p = calculaAreaPerimetro(x, y)
    print(f'Área: {a:.2f} cm2   Perímetro: {p:.2f} cm')

primos = 0

for i in range (1, 11):
    n = restricaoN(int(input(f'Digite o valor do {i}º número: ')))
    if isPrimo(n):
        print(f'{n} é primo!')
        primos += 1
    else:
        print(f'{n} não é primo!')
    print(f'\n')

print(f'Total de primos: {primos}')

