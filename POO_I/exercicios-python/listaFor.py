# Lista de exercícios estrutura de repetição For

for ano in range(2004, 2100, 4):
    print(ano)

for i in range(1, 50, 2):
    print(i)

nota  = -1
aluno = ""
mensalidade = -1

for i in range(0, 5, 1):
    a = input("Digite o nome do aluno: ")
    b = float(input("Digite a nota/média geral do aluno: "))
    c = float(input("Digite a mensalidade do aluno: "))

    if b > nota:
        nota = b
        aluno = a
        mensalidade = c

    print()

valorFinal = mensalidade - mensalidade*0.3

print(f'ALUNO: {aluno} \nMENSALIDADE SEM DESCONTO = R$ {mensalidade:.2f} \nDESCONTO 30% = R$ {valorFinal:.2f}')

par = 0
impar = 0
for i in range(0, 10, 1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Quantidade de pares = {par} \nQuantidade de ímpares = {impar}')

n = int(input('Digite um número: '))
verif = False

for i in range (n -1, 0, -1):
    if n % i == 0 and i != 1:
        verif = False
        break
    else:
        verif = True

if verif:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')

n = int(input('Digite um número: '))
verif = True

for i in range (n -1, 0, -1):
    if n % i == 0 and i != 1:
        verif = False
        print(f'Divisível por {i}')

if verif:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')

n = int(input('Digite o número de pessoas da turma: '))
media = 0

for i in range(1, n+1, 1):
    idade = int(input(f'Digite a idade da {i}º pessoa: '))
    media += idade

media = media/n

if media <= 25:
    print("TURMA JOVEM")
elif media > 25 and media <= 60:
    print("TURMA ADULTA")
else:
    print("TURMA IDOSA")

n1 = int(input('Digite o valor de N1: '))
n2 = int(input('Digite o valor de N2: '))
soma = 0

for i in range(n1, n2+1, 1):
    print(f'{i}', end=", ")
    soma += i

print(f'\nSOMA = {soma}')

n = int(input('Digite um número para gerar sua tabuada: '))

for i in range(1, 11, 1):
    print(f'{i} X {n} = {i*n}')

aluno = ""
nota = -1
media = 0

for i in range(1, 6, 1):
    a = input(f'Nome do {i}º aluno: ')
    b = float(input(f'Nota do {i}º aluno: '))
    media += b
    if b > nota:
        nota = b
        aluno = a
    print()

media = media / 5
print(f'\nMÉDIA DA TURMA = {media:.2f}\n')

if nota >= 5.75:
    print(f'{aluno} - APROVADO')
elif nota >= 2.75 and nota < 5.75:
    print(f'{aluno} - RECUPERAÇÃO')
else:
    print(f'{aluno} - REPROVADO')

maior = -1
menor = 100000
media = 0

n = int(input('Digite o número de valores a ser informado: '))

for i in range(1, n+1, 1):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    media += valor

media = media / n

print(f'\nMÉDIA DE VALORES = {media:.2f} \nMAIOR VALOR = {maior} \nMENOR VALOR = {menor}')

n = int(input('Digite o número de praias que você quer cadastrar: '))
maiorDist = -1
praiaMaiorDist = ""
media = 0
praias15_20 = ""

for i in range(1, n+1, 1):
    nome = input(f'Digite o nome da {i}º praia: ')
    dist = float(input(f'Digite a distância da praia {nome} até o centro da cidade: '))
    media += dist
    if dist > maiorDist:
        maiorDist = dist
        praiaMaiorDist = nome
    
    if dist >= 15 and dist <= 20:
        praias15_20 = f'{praias15_20} {nome},'

media = media/n

print(f'\nMÉDIA = {media:.2f} \nPRAIA MAIS LONGE: {praiaMaiorDist} \nPRAIAS À 15-20KM: {praias15_20}')
