#Lista de exercícios - Estrutura Condicional

import math

valor = float(input('Digite o valor da casa: '));
sal = float(input('Digite o salário do comprador: '));
anos = int(input('Em quantos anos será pago: '));
parcela = valor/(anos*12);
print();
if parcela > sal*0.3:
    print('EMPRÉSTIMO NEGADO');
else:
    print(f'EMPRÉSTIMO ACEITO \nPARCELA = R$ {parcela:.2f}');

print();

valor = float(input('Digite o valor do produto: '));
op = input('CONDIÇÃO DE PAGAMENTO: \na - à vista \nb - 1x no cartão \nc - 2x no cartão \nd - 3x ou mais no cartão \nESCOLHA: ');
print();
if op == 'a':
    valor -= valor*0.1;
    print(f'VALOR FINAL DO PRODUTO = R$ {valor:.2f}');
elif op == 'b':
    valor -= valor*0.05;
    print(f'VALOR FINAL DO PRODUTO = R$ {valor:.2f}');
elif op == 'c':
    valor = valor;
    print(f'VALOR FINAL DO PRODUTO = R$ {valor:.2f}');
elif op == 'd':
    valor += valor*0.2;
    print(f'VALOR FINAL DO PRODUTO = R$ {valor:.2f}');
else:
    print('OPÇÃO INEXISTENTE!');
print();

altura = float(input('ALTURA: '));
peso = float(input('PESO: '));
imc = peso/(altura*altura);
print();
if imc <= 18.5:
    print('ABAIXO DO PESO');
elif imc > 18.5 and imc <= 25:
    print('PESO IDEAL');
elif imc > 25 and imc <= 30:
    print('SOBREPESO');
elif imc > 30 and imc <= 40:
    print('OBESIDADE');
else:
    print('OBESIDADE MÓRBIDA');
print();
    
n1 = float(input('NOTA 1: '));
n2 = float(input('NOTA 2: '));
n3 = float(input('NOTA 3: '));
media = (n1+n2+n3)/3;
print();
if media < 5:
    print('REPROVADO');
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO');
else:
    print('APROVADO');
print();

imposto = 0
valor = float(input('VALOR RECEBIDO: '))

if valor > 2000:
    valor -= 2000
    if valor > 1000:
        imposto += 1000*0.08
    else:
        imposto += valor*0.08
    valor -= 1000

    if valor > 0:
        if valor > 1500:
            imposto += 1500*0.18
        else:
            imposto += valor*0.18
        valor -= 1500

        if valor > 0:
            imposto += valor*0.28


if imposto > 0:
    print(f'IMPOSTO A SER PAGO = R$ {imposto:.2f}')
else:
    print('ISENTO')
print()

dIn = int(input('Informe o dia de início do evento: '))
horarioInicio = input('Informe o horário do início no formato "hh:mm:ss": ')
hIn = int(horarioInicio[0:2])
mIn = int(horarioInicio[3:5])
sIn = int(horarioInicio[6:8])
dFim = int(input('Informe o dia de término do evento: '))
horarioFim = input('Informe o horário de término do evento no formato "hh:mm:ss": ')
hFim = int(horarioFim[0:2])
mFim = int(horarioFim[3:5])
sFim = int(horarioFim[6:8])

segundos = sIn
minutos = mIn
horas = hIn
dias = dIn

if segundos > 0:
    segundos = 60 - segundos
    minutos = minutos + 1

if minutos > 0:
    minutos = 60 - minutos
    horas = horas + 1

if horas > 0:
    horas = 24 - horas
    dias = dias + 1

dias = dFim - dias

horas = horas + hFim
minutos = minutos + mFim
segundos = segundos + sFim

if segundos >= 60:
    minutos = minutos + int(segundos/60)
    segundos = segundos - 60*int(segundos/60)

if minutos >= 60:
    horas = horas + int(minutos/60)
    minutos = minutos - 60*int(minutos/60)

if horas >= 24:
    dias = dias + int(horas/24)
    horas = horas - 24*int(horas/24)

print(f'DIA(S): {dias} \nHORA(S): {horas} \nMINUTO(S): {minutos} \nSEGUNDO(S): {segundos}')
print()

ddd = input('Digite o DDD: ')
if(ddd == '61'):
    print('DDD: Brasília')
elif(ddd == '71'):
    print('DDD: Salvador')
elif(ddd == '21'):
    print('DDD: Rio de Janeiro')
elif(ddd == '11'):
    print('DDD: São Paulo')
elif(ddd == '32'):
    print('DDD: Juiz de Fora')
elif(ddd == '19'):
    print('DDD: Campinas')
elif(ddd == '27'):
    print('DDD: Vitória')
elif(ddd == '31'):
    print('DDD: Belo Horizonte')
else:
    print('DDD NÃO LOCALIZADO')
print()

mes = input('Digite o número do mês: ')
if(mes == "1"):
    print("Janeiro")
elif(mes == "2"):
    print("Fevereiro")
elif(mes == "3"):
    print("Março")
elif(mes == "4"):
    print("Abril")
elif(mes == "5"):
    print("Maio")
elif(mes == "6"):
    print("Junho")
elif(mes == "7"):
    print("Julho")
elif(mes == "8"):
    print("Agosto")
elif(mes == "9"):
    print("Setembro")
elif(mes == "10"):
    print("Outubro")
elif(mes == "11"):
    print("Novembro")
elif(mes == "12"):
    print("Dezembro")
else:
    print("Mês incorreto.")

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b*b) -4*a*c
if(delta < 0 or a == 0):
    print("IMPOSSÍVEL DE CALCULAR")
else:
    raiz = math.sqrt(delta)
    x1 = (-b + raiz)/2*a;
    x2 = (-b - raiz)/2*a;
    print(f'X1 = {x1} \nX2 = {x2}')
print()

c1 = int(input('Competidor 1: '))
c2 = int(input('Competidor 2: '))
c3 = int(input('Competidor 3: '))

if (c1 > c2 and c1 < c3) or (c1 > c3 and c1 < c2):
    print(c1)
elif (c2 > c1 and c2 < c3) or (c2 > c3 and c2 < c1):
    print(c2)
elif (c3 > c2 and c3 < c1) or (c3 > c1 and c3 < c2):
    print(c3)

vF = int(input("Digite o número de vitórias do Flamengo: "))
sF = int(input("Digite o saldo de gols do Flamengo: "))
eF = int(input("Digite o número de empates do Flamengo: "))
vC = int(input("Digite o número de vitórias do Corinthians: "))
sC = int(input("Digite o saldo de gols do Corinthians: "))
eC = int(input("Digite o número de empates do Corinthians: "))

pF = vF*3 + eF
pC = vC*3 + eC

if pF != pC:
    if pF > pC:
        print("F")
    else:
        print("C")
else:
    if sC != sF:
        if sC > sF:
            print("C")
        else:
            print("F")
    else:
        print("=")

D = int(input("Digite o dia: "))
pI = int(input("Digite o preço inicial: "))
x = int(input("Digite a variação diária: "))
F = int(input("Digite o número de dias a ser previsto: "))

if D % 2 == 0:
    if F % 2 == 0:
        print(pI)
    else:
        pI -= x
        print(pI)
else:
    if F % 2 == 0:
        print(pI)
    else:
        pI += x
        print(pI)
    
l1 = input("Primeira linha do dado (números separados com espaços): ")
l2 = input("Segunda linha do dado (números separados com espaços): ")
l3 = input("Terceira linha do dado (números separados com espaços): ")
dado = [l1.split(" "), l2.split(" "), l3.split(" ")]
nums = [];
nums.extend(dado[0])
nums.extend(dado[1])
nums.extend(dado[2])

verif = False

if len(nums) == 6:
    if nums.count("1") == 1:
        if nums.count ("2") == 1:
            if nums.count("3") == 1:
                if nums.count("4") == 1:
                    if nums.count("5") == 1:
                        if nums.count("6") == 1:
                            if int(dado[0][0]) + int(dado[2][0]) == 7:
                                if int(dado[1][0]) + int(dado[1][2]) == 7:
                                    if int(dado[1][1]) + int(dado[1][3]) == 7:
                                        verif = True

if verif:
    print("SIM")
else:
    print("NÃO")

hIn = int(input('Digite a hora de início: '))
hFim = int(input('Digite a hora de término: '))
horasJogo = 0

if hIn > hFim:
    horasJogo = (24 - hIn) + hFim
elif hIn == hFim:
    horasJogo = 24
else:
    horasJogo = hFim - hIn

print(f"O jogo durou {horasJogo} hora(s).")

horarioIn = input('Digite o horário de início (formato "hh:mm"): ')
horarioFim = input('Digite o horário de término (formato "hh:mm"): ')
hIn = int(horarioIn[0:2])
mIn = int(horarioIn[3:5])
hFim = int(horarioFim[0:2])
mFim = int(horarioFim[3:5])

horas = hIn
minutos = mIn

if minutos > 0:
    minutos = 60 - minutos
    horas = horas + 1

horas = hFim - horas
minutos = minutos + mFim

if minutos >= 60:
    horas = horas + int(minutos/60)
    minutos = minutos - 60*int(minutos/60)

if horas == 0 and minutos == 0:
    horas = 24

print(f'O jogo durou {horas} hora(s) e {minutos} minuto(s).')

d = int(input('Digite o diâmetro da bola: '))
l = int(input('Digite a largura da caixa: '))
a = int(input('Digite a altura da caixa: '))
p = int(input('Digite a profundidade da caixa: '))

verif = False
if l >= d:
    if a >= d:
        if p >= d:
            verif = True

if verif:
    print("S")
else:
    print("N")

sal = float(input('Digite seu salário: '))
reajuste = 0
pct = 0

if sal <= 400:
    reajuste = sal*0.15
    pct = 15
elif sal > 400 and sal <= 800:
    reajuste = sal*0.12
    pct = 12
elif sal > 800 and sal <= 1200:
    reajuste = sal*0.1
    pct = 10
elif sal > 1200 and sal <= 2000:
    reajuste = sal*0.07
    pct = 7
else:
    reajuste = sal*0.04
    pct = 4

sal += reajuste

print(f'Novo salário: R$ {sal:.2f} \nReajuste ganho: R$ {reajuste:.2f} \nEm %: {pct}')

eC = int(input('Digite a espessura do colchão: '))
lC = int(input('Digite a largura do colchão: '))
hC = int(input('Digite a altura do colchão: '))
hP = int(input('Digite a altura da porta: '))
lP = int(input('Digite a largura da porta: '))

if lC <= hP and eC <= lP:
    print('S')
else:
    print('N')

A = int(input('Digite o valor da variável A: '))
B = int(input('Digite o valor da variável B: '))
C = int(input('Digite o valor da variável C: '))
D = int(input('Digite o valor da variável D: '))

if B > C and D > A and C+D > A+B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos!")
else:
    print("Valores negados!")

cod = input("Digite o código do produto: ")
qnt = int(input("Digite a quantidade deste produto: "))
total = 0

if cod == "1":
    total += qnt*4
elif cod == "2":
    total += qnt*4.5
elif cod == "3":
    total += qnt*5
elif cod == "4":
    total += qnt*2
elif cod == "5":
    total += qnt*1.5
else:
    total = -1

if total > 0:
    print(f'TOTAL = R$ {total:.2f}')
else:
    print("PRODUTO INEXISTENTE")

comp = int(input("Digite o número de competidores: "))
fTotais = int(input("Digite a quantidade total de folhas: "))
fComp = int(input("Digite o número de folhas por competidor: "))

if fTotais >= fComp*comp:
    print("S")
else:
    print("N")

n1 = float(input('Digite o valor da variável A: '))
n2 = float(input('Digite o valor da variável B: '))
n3 = float(input('Digite o valor da variável C: '))

list = [n1, n2, n3]
list.sort()
A = list[2]
B = list[1]
C = list[0]

if A >= B+C:
    print("NÃO FORMA TRIÂNGULO")
else:
    if A*A == (B*B) + (C*C):
        print("TRIÂNGULO RETÂNGULO")

    if A*A > (B*B) + (C*C):
        print("TRIÂNGULO OBTUSÂNGULO")

    if A*A < (B*B) + (C*C):
        print("TRIÂNGULO ACUTÂNGULO")

    if A == B and B == C:
        print("TRIÂNGULO EQUILÁTERO")

    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("TRIÂNGULO ISÓSCELES")