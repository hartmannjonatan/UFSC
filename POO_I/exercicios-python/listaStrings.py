# LISTA STRING

def viraDireita(pos):
    if pos == 'N':
        pos = 'L'
    elif pos == 'L':
        pos = 'S'
    elif pos == 'S':
        pos = 'O'
    elif pos == 'O':
        pos = 'N'

def viraEsquerda(pos):
    if pos == 'N':
        pos = 'O'
    elif pos == 'O':
        pos = 'S'
    elif pos == 'S':
        pos = 'L'
    elif pos == 'L':
        pos = 'N'
    
    return pos

def contarLeds(num):
    num = int(num)
    if num == 0:
        return 6
    elif num == 1:
        return 2
    elif num == 2:
        return 5
    elif num == 3:
        return 5
    elif num == 4:
        return 4
    elif num == 5:
        return 5
    elif num == 6:
        return 6
    elif num == 7:
        return 3
    elif num == 8:
        return 7
    elif num == 9:
        return 6
    
def multipleThree(n, m):
    soma = 0
    for i in range(0, int(n)):
        soma += int(m[i])
    print(f'{soma}', end=" ")

    if len(str(soma)) > 1:
        multipleThree(soma)
    else:
        if soma == 3 or soma == 6 or soma == 9:
            print('SIM')
        else:
            print('NÃO')
        
    
n = int(input('Digite o número de passos: '))
s = input('Digite a sequência [sem espaços]: ')
pos = 'N'  #Posição inicial

for i in range(0, n):
    if(s[i].upper == 'D'):
        pos = viraDireita(pos)
    else:
        pos = viraEsquerda(pos)
    
print(f'\nFinal: {pos}')

n = int(input('Digite o número de casos de teste: '))

for i in range(1, n+1):
    result = 0
    s = input(f'Digite a {i}º sequência: ')
    if s[0] == s[2]:
        result = int(s[0])*int(s[2])
    else:
        if s[1].isupper():
            result = int(s[2])-int(s[0])
        else:
            result = int(s[2])+int(s[0])
    print(f'Resposta: {result}\n')

n = int(input('Digite o número de casos de teste: '))

for i in range(1, n+1):
    num = input('Digite o número a ser contado seus leds: ')
    leds = 0
    for j in range(0, len(num)):
        leds += contarLeds(num[j])
    print(f'Para o número {num} são necessários {leds} leds.\n')

n = int(input('Digite o número de casos de teste: '))
c = 0
s = 0
r = 0
total = 0

for i in range(1, n+1):
    q, a = input('Digite o número e o caractere do animal separado por espaço: ').split(' ')
    if a.upper() == "C":
        c += int(q)
    elif a.upper() == "S":
        s += int(q)
    elif a.upper() == "R":
        r += int(q)

    total += int(q)

print(f'TOTAL DE COBAIAS: {total} \nTotal de coelhos: {c} ({((c*100)/total):.2f} %) \nTotal de sapos: {s} ({((s*100)/total):.2f} %) \nTotal de ratos: {r} ({((r*100)/total):.2f} %)')

while True:
    n, m = input('Digite o número de algarismos de m, e m separados por espaços: ').split()
    multipleThree(n, m)
    aux = input('Deseja continuar testando: [0 - Não, 1 - Sim]: ')
    if aux == '0':
        break
