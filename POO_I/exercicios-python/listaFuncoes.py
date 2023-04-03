# Lista Funções

# SEM RETURN

def novoSal(sal):
    novoSal = sal
    p = 0
    if sal <= 400:
        novoSal += sal*0.15
        p = 15
    elif novoSal <= 800:
        novoSal += sal*0.12
        p = 12
    elif sal <= 1200:
        novoSal += sal*0.1
        p = 10
    elif sal <= 2000:
        novoSal += 0.07
        p = 7
    else:
        novoSal += 0.04
        p = 4

    print(f'Novo salário: R$ {novoSal:.2f} \nReajuste: R$ {(novoSal-sal):.2f} \nEm percentual: {p}%')

def calculaTempo(s, t, f):
    tempo = s + t + f
    if tempo == 24:
        tempo = 0
    elif tempo < 0:
        tempo = 24 + tempo
    elif tempo > 24:
        tempo = tempo - 24
    
    print(f'{tempo} hora(s).')

def ultrapassandoZ(x, z):
    while x > z:
        z = int(input('Digite Z: '))
    
    if z > x:
        count = 2
        aux = x
        while True:
            count += 1
            aux += x+count
            if aux > z:
                print(count)
                break

def verificarQuadrante(x, y):
    x = int(x)
    y = int(y)
    if x == 0 or y == 0:
        print("Fim!")
    else:
        if x > 0 and y > 0:
            print(f"({x}, {y}) = 1º Quadrante")
        elif x < 0 and y > 0:
            print(f"({x}, {y}) = 2º Quadrante")
        elif x < 0 and y < 0:
            print(f"({x}, {y}) = 3º Quadrante")
        elif x > 0 and y < 0:
            print(f"({x}, {y}) = 4º Quadrante")
        
        verificarQuadrante(int(input('Digite o valor de x [0 para terminar]: ')), int(input('Digite o valor de y [0 para terminar]: ')))

def elevador(sensores, capacidade):
    pessoas = 0
    verif = "N"
    for i in range(1, sensores+1):
        print(f'{i}º LEITURA:')
        pessoas += int(input('Entradas: '))
        pessoas -= int(input('Saídas: '))
        if pessoas > capacidade:
            verif = "S"
    
    print(verif)

def contador(inicio, fim, passo):
    if fim < inicio:
        for i in range(inicio, fim-1, -passo):
            print(i, end=" ")
    else:
        for i in range(inicio, fim+1, passo):
            print(i, end=" ")
    print("\nFim!")

def area(b, h):
    print(f'Área do terreno = {(b*h):.2f}')


# COM RETURN

def colchao(a, b, c, h, l):
    if l > a and h > b:
        return "S"
    else:
        return "N"
    
def mediaMelhor():
    m = 0.0
    melhor = -1
    for i in range(1, 6):
        aux = float(input(f'Digite a nota do {i}º aluno: '))
        m += aux
        if aux > melhor:
            melhor = aux
    m = m/5
    
    return f'{m:.2f} {melhor:.2f}'

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def primo(n):
    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return False
            break
    
    return True
    
def quantidadePrimosIntervalo(inicio, fim):
    if inicio == 1:
        inicio += 1
    count = 0
    for n in range(inicio, fim+1):
        if primo(n):
            count += 1
    
    return count

def mediaIdade():
    media = 0
    count = 0
    while True:
        idade = int(input('Digite a idade [negativo para encerrar]: '))
        if idade < 0:
            break
        else:
            media += idade
            count += 1
    
    media = media/count
    return media

def valoresFloat():
    positivo = 0
    media = 0
    for i in range(1, 7):
        valor = float(input(f'Digite o {i}º valor: '))
        if valor > 0:
            positivo += 1
        media += valor
    media = media/6
    return f'{media:.2f} {positivo:.2f}'


# PROGRAMA PRINCIPAL

novoSal(float(input('Digite seu salário: R$ ')))
calculaTempo(int(input('Digite a hora de partida: ')), int(input('Digite o tempo da viagem: ')), int(input('Digite o fuso horário: ')))
ultrapassandoZ(int(input('Digite X: ')), int(input('Digite Z: ')))
verificarQuadrante(int(input('Digite o valor de x [0 para terminar]: ')), int(input('Digite o valor de y [0 para terminar]: ')))
elevador(int(input('Digite a quantidade de leituras do sensor: ')), int(input('Digite a capacidade máxima de pessoas: ')))
print(colchao(int(input('Digite A: ')), int(input('Digite B: ')), int(input('Digite C: ')), int(input('Digite h: ')), int(input('Digite l: '))))

n = mediaMelhor()
media = n.split(" ")[0]
melhor = n.split(" ")[1]
status = ""
print(f'Média da turma: {media}')
if float(melhor) >= 5.75:
    status = "Aprovado"
elif float(melhor) >= 2.75:
    status = "Recuperação"
else:
    status = "Reprovado"

print(f'Melhor nota: {melhor} | {status}')

npar = 0
nimpar = 0
for i in range(1, 11):
    if par(int(input(f'Digite o {i}º número: '))):
        npar += 1
    else:
        nimpar += 1

print(f'Números pares = {npar} \nNúmeros ímpares = {nimpar}')

count = quantidadePrimosIntervalo(int(input('Início: ')), int(input('Fim: ')))
print(f'Quantidade de números primos entre esse intervalo: {count}')
print(f'Média das idades: {mediaIdade():.2f}')

n = valoresFloat()
media = n.split(" ")[0]
positivo = n.split(" ")[1]
print(f'Média dos valores: {media} \nNúmeros positivos: {positivo}')

# Contagem 1 - 10 (de 1 em 1)
contador(1, 10, 1)
# Contagem 10 - 1 (de 1 em 1)
contador(10, 1, 1)
# Contagem personalizada
contador(int(input('Digite o valor de início: ')), int(input('Digite o valor final: ')), int(input('Digite o passo: ')))

area(float(input('Digite o valor da base: ')), float(input('Digite o valor da altura: ')))