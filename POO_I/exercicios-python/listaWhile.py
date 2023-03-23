# Lista de exercícios de while

import random

s = input("Digite seu sexo [F/M]: ").upper()
while s != "M" and s != "F":
    s = input("Formato incorreto, digite novamente [F/M]: ").upper()


n = random.randint(0, 10)
count = 1
aux = int(input("Digite um número de 0 a 10: "))
while aux != n:
    aux = int(input("Número incorreto! Digite novamente: "))
    count += 1

print(f'Parabéns você descobriu o número sorteado. \nO número era {n}. \nVocê fez {count} tentativa(s). ')

next = "S"
while next == "S":
    sal = float(input('Digite o salário do funcionário: '))
    perc = 11
    desc = sal*0.11
    if desc > 320:
        desc = 320
        perc = 32000/sal

    print(f'Desconto de {perc:.1f}% sobre o salário = {desc:.2f} R$')
    next = input('Deseja calcular um novo desconto [S/N]: ').upper()
    print()

n = int(input('Digite um número: '))
for i in range(1, 10001, 1):
    if i % n == 2:
        print(i)

n = int(input('Digite um número: '))
i = 1

while i <= 10:
    print(f'{i} X {n} = {i*n}')
    i += 1

n = int(input('Digite um número: '))
while n != 0:
    for i in range(1, n+1, 1):
        print(i, end=" ")
    print()
    n = int(input('Digite outro número: '))

print('Programa finalizado!')

n = int(input(f'Qual sua preferência: \n1- Álcool \n2- Gasolina \n3- Diesel \n4- Finalizar \n\nEscolha: '))
alcool = 0
gasolina = 0
diesel = 0
while n != 4:
    if n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1
    else:
        print('\nCódigo inválido!\n')
    
    n = int(input(f'Qual sua preferência: \n1- Álcool \n2- Gasolina \n3- Diesel \n4- Finalizar \n\nEscolha: '))

print(f'\nPROGRAMA FINALIZADO! \nÁlcool: {alcool} cliente(s) \nGasolina: {gasolina} cliente(s) \nDiesel: {diesel} cliente(s)')

m = int(input('Digite o primeiro número: '))
n = int(input('Digite o segundo número: '))

while m > 0 and n > 0:
    soma = 0
    if m <= n:
        for i in range(m, n+1, 1):
            soma += i
            print(f'{i}', end=" ")
    else:
        for i in range(n, m+1, 1):
            soma += i
            print(f'{i}', end=" ")

    
    print(f'\nSoma consecutiva = {soma}\n')

    m = int(input('Digite o primeiro número: '))
    n = int(input('Digite o segundo número: '))

print('\nPrograma finalizado!')