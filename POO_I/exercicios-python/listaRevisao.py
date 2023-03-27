# Lista Exercícios 05 - Revisão IF, FOR, WHILE

import math

n1 = int(input('Digite N1: '))
n2 = int(input('Digite N2: '))

while n1 != n2:
    if(n1 < n2):
        print(f'{n1} - {n2}: CRESCENTE')
    else:
        print(f'{n1} - {n2}: DECRESCENTE')

    print()
    n1 = int(input('Digite N1: '))
    n2 = int(input('Digite N2: '))

print('\nPROGRAMA ENCERRADO')

n = int(input('Digite o número de caso de testes: '))

for i in range(0, n):
    n1 = int(input('Digite N1: '))
    n2 = int(input('Digite N2: '))
    sum = 0
    for j in range(n1+1, n2):
        if j%2 != 0:
            sum += j
    print(f'SOMA ({n1}, {n2}) ÍMPARES: {sum}')

n = int(input('Digite o número de casos de teste: '))

for i in range(0, n):
    D = int(input('Digite a distância entre ambos os barcos: '))
    VF = int(input('Digite a velocidade do barco desgovernado: '))
    VG = int(input('Digite a velocidade do barco da guarda costeira: '))

    tVF = float(12/VF)
    tVG = float((math.sqrt(144 + (D*D)))/VG)

    if(tVG <= tVF):
        print('S')
    else:
        print('N')

v = float(input('Digite o valor em R$: '))
aux = 0
print(f'\nNOTAS:')

while v >= 2:
    if(int(v/100) >= 1):
        aux = int(v/100)
        print(f'100.00 R$: {aux} nota(s)')
    v -= int(v/100)*100
    
    if(int(v/50) >= 1):
        aux = int(v/50)
        print(f'50.00 R$: {aux} nota(s)')
    v -= int(v/50)*50

    if(int(v/20) >= 1):
        aux = int(v/20)
        print(f'20.00 R$: {aux} nota(s)')
    v -= int(v/20)*20


    if(int(v/10) >= 1):
        aux = int(v/10)
        print(f'10.00 R$: {aux} nota(s)')
    v -= int(v/10)*10

    if(int(v/5) >= 1):
        aux = int(v/5)
        print(f'05.00 R$: {aux} nota(s)')
    v -= int(v/5)*5
    
    if(int(v/2) >= 1):
        aux = int(v/2)
        print(f'02.00 R$: {aux} nota(s)')
    v -= int(v/2)*2

print('MOEDAS:')

while v != 0:
    if(int(v/1) >= 1):
        aux = int(v/1)
        print(f'01.00 R$: {aux} moeda(s)')
        v -= int(v/1)*1
        v = format(v, '.2f')
        v= float(v)

    if(int(v/0.5) >= 1):
        aux = int(v/0.5)
        print(f'00.50 R$: {aux} moeda(s)')
        v -= float(int(v/0.5)*0.5)
        v = format(v, '.2f')
        v= float(v)


    if(int(v/0.25) >= 1):
        aux = int(v/0.25)
        print(f'00.25 R$: {aux} moeda(s)')
        v -= float(int(v/0.25)*0.25)
        v = format(v, '.2f')
        v= float(v)


    if(int(v/0.10) >= 1):
        aux = int(v/0.10)
        print(f'00.10 R$: {aux} moeda(s)')
        v -= float(int(v/0.10)*0.10)
        v = format(v, '.2f')
        v= float(v)


    if(int(v/0.05) >= 1):
        aux = int(v/0.05)
        print(f'00.05 R$: {aux} moeda(s)')
        v -= float(int(v/0.05)*0.05)
        v = format(v, '.2f')
        v= float(v)


    if(int(v/0.01) >= 1):
        aux = int(v/0.01)
        print(f'00.01 R$: {aux} moeda(s)')
        v -= float(int(v/0.01)*0.01)
        v = format(v, '.2f')
        v= float(v)

p1 = float(input('Digite o tempo que o piloto mais rápido leva para dar uma volta: '))
p2 = float(input('Digite o tempo que o piloto mais devagar leva para dar uma volta: '))
v1 = 1
v2 = 1

t = 0

while v1 == v2:
    t += p2
    v2 += 1
    v1 += int(t/p1)

print(f'Volta do piloto retardatário: {v1}')

n1 = float(input('Digite N1: '))
n2 = float(input('Digite N2: '))
n3 = float(input('Digite N3: '))
n4 = float(input('Digite N4: '))
n5 = float(input('Digite N5: '))

maior = -1
menor = 10000

if(n1 > maior):
    maior = n1
if n1 < menor:
    menor = n1

if(n2 > maior):
    maior = n2
if n2 < menor:
    menor = n2

if(n3 > maior):
    maior = n3
if n3 < menor:
    menor = n3

if(n4 > maior):
    maior = n4
if n4 < menor:
    menor = n4

if(n5 > maior):
    maior = n5
if n5 < menor:
    menor = n5

total = (n1+n2+n3+n4+n5) - (maior+menor)

print(f'A soma das notas excluindo a maior e a menor nota: {total:.2f}')

n = int(input('Digite o número de Depósitos: '))
j = 0
z = 0
print()

for i in range(1, n+1):
    j += int(input(f'TESTE {i}: \nValor (em centavos) para João: '))
    z += int(input(f'Valor (em centavos) para Zézinho: '))
    print(f'Diferença = {j-z}')
    print()

v = float(input('Digite o valor solicitado em R$: '))

aux = 0
print(f'\nNOTAS:')

if(int(v/50) >= 1):
    aux = int(v/50)
    print(f'50.00 B$: {aux} nota(s)')
v -= int(v/50)*50


if(int(v/10) >= 1):
    aux = int(v/10)
    print(f'10.00 B$: {aux} nota(s)')
v -= int(v/10)*10

if(int(v/5) >= 1):
    aux = int(v/5)
    print(f'05.00 B$: {aux} nota(s)')
v -= int(v/5)*5

if(int(v/1) >= 1):
    aux = int(v/1)
    print(f'01.00 B$: {aux} nota(s)')
v -= int(v/1)*1


x = int(input('Digite x: '))
z = int(input('Digite z: '))
count = 0
sum = -1

while z <= x:
    z = int(input('Digite z: '))

for i in range(x, z+1):
    sum += i
    count += 1
    if sum >= z:
        break

print(count)

x = int(input('Digite a coordenada x: '))
y = int(input('Digite a coordenada y: '))

if((x >= 0) and (x <= 432)) and ((y >= 0) and (y <= 468)):
    print('Dentro')
else:
    print('Fora')

p = int(input('Digite a posição da portinha P (0 ou 1): '))
r = int(input('Digite a posição da portinha R (0 ou 1): '))
c = ''

if p == 0:
    c = 'C'
else:
    if r == 0:
        c = 'B'
    else:
        c = 'A'

print(f'Caminho final = {c}')

n = int(input('Digite o número de bandejas: '))
copos = 0

for i in range(1, n+1):
    l = int(input(f'BANDEJA {i}: \nLatas: '))
    c = int(input('Copos: '))
    if l > c:
        copos += c

print(f'Total de copos quebrados: {copos}')

q = int(input('Digite o número de quadrados em cada lado da grade: '))
total = 0

while q != 0:
    total = (q*(q+1)*((2*q)+1))/6
    print(total)

    q = int(input('Digite o número de quadrados em cada lado da grade: '))

vA = float(input('Digite (em R$) o valor do álcool: '))
vG = float(input('Digite (em R$) o valor da gasolina: '))
a = float(input('Digite quantos km/l faz o carro com o álcool: '))
g = float(input('Digite quantos km/l faz o carro com a gasolina: '))

if vG >= vA:
    aux = (vG*a)/vA
    if aux > g:
        print('A')
    else:
        print('G')
else:
    print('G')

verif = 's'

while verif == 's':
    print(f'\nJOGADOR 1:')
    e1 = int(input('1 - Pedra \n2 - Papel \n3 - Tesoura \n   Escolha: '))

    print(f'\nJOGADOR 2:')
    e2 = int(input('1 - Pedra \n2 - Papel \n3 - Tesoura \n   Escolha: '))

    if(e1 == 1):
        if(e2 == 1):
            print('\nEMPATE\n')
        elif(e2 == 2):
            print('JOGADOR 2 GANHOU!')
        else:
            print('JOGADOR 1 GANHOU!')
    elif(e1 == 2):
        if(e2 == 2):
            print('\nEMPATE\n')
        elif(e2 == 3):
            print('JOGADOR 2 GANHOU!')
        else:
            print('JOGADOR 1 GANHOU!')
    else:
        if(e2 == 3):
            print('\nEMPATE\n')
        elif(e2 == 1):
            print('JOGADOR 2 GANHOU!')
        else:
            print('JOGADOR 1 GANHOU!')

    verif = input('Deseja jogar novamente [s/n]: ')

n1 = int(input('Digite N1: '))
n2 = int(input('Digite N2: '))
n3 = int(input('Digite N3: '))

maior = -1
menor = 1000
meio = -1

if n1 > n2 and n1 > n3:
    if n2 < n3:
        menor = n2
        meio = n3
    else:
        menor = n3
        meio = n2
    maior = n1
elif n1 < n2 and n1 < n3:
    if n2 > n3:
        maior = n2
        meio = n3
    else:
        maior = n3
        meio = n2
    menor = n1
elif n2 > n1 and n2 > n3:
    if n1 < n3:
        menor = n1
        meio = n3
    else:
        menor = n3
        meio = n1
    maior = n2
elif n2 < n1 and n2 < n3:
    if n1 > n3:
        maior = n1
        meio = n3
    else:
        maior = n3
        meio = n1
    menor = n2
elif n3 > n1 and n3 > n2:
    if n1 < n2:
        menor = n1
        meio = n2
    else:
        menor = n2
        meio = n1
    maior = n3
else:
    if n1 > n2:
        maior = n1
        meio = n2
    else:
        maior = n2
        meio = n1
    menor = n3

print(f'VALORES ORDENADOS: {menor}, {meio}, {maior};')


    