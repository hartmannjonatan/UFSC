#Lista de exercícios: Estrutura Sequencial

import math;

A = int(input("Digite o valor da variável A: "));
print();
B = int(input("Digite o valor da variável B: "));
soma = A + B;
print();
print(f'SOMA = {soma}');

prod = A*B;
print();
print(f'PRODUTO = {prod}');
print();

A = float(input('Digite o valor da variável A: '));
print();
B = float(input('Digite o valor da variável B: '));
media = ((A*3.5) + (B*7.5))/11;
print();
print(f'MÉDIA = {media:.1f}');
print();

A = float(input('Digite o valor da variável A: '));
print();
B = float(input('Digite o valor da variável B: '));
print();
C = float(input('Digite o valor da variável C: '));
media = ((A*2) + (B*3) + (C*5))/10;
print();
print(f'MÉDIA = {media:.1f}');
print();

A = int(input('Digite o valor da variável A: '));
print();
B = int(input('Digite o valor da variável B: '));
print();
C = int(input('Digite o valor da variável C: '));
print();
D = int(input('Digite o valor da variável D: '));
total = (A*B) - (C*D);
print();
print(f'RESULTADO = {total}');
print();

num = int(input('Digite o número do funcionário: '));
horas = int(input('Digite a quantidade de horas trabalhadas: '));
valor = float(input('Digite o valor recebido por horas: '));
sal = horas*valor;
print();
print(f'NÚMERO: {num} \nSALÁRIO = R$ {sal:.2f}');
print();

N = int(input('Digite a pressão desejada: '));
M = int(input('Digite a pressão atual: '));
pressao = N - M;
print();
print(f'Pressão a ser colocada: {pressao}');
print();

t = int(input('Informe o total de pessoas que clicaram no terceiro link: '));
pessoas = t*4;
print();
print(f'Total de pessoas que clicaram no primeiro link = {pessoas}');
print();

A = float(input('Digite o valor da variável A: '));
print();
B = float(input('Digite o valor da variável B: '));
print();
C = float(input('Digite o valor da variável C: '));
print();
aTr = A*C/2;
aC = 3.14159*(C*C);
aT = ((A + B)*C)/2;
aQ = B*B;
aR = A*B;
print();
print(f'ÁREA DO TRIÂNGULO = {aTr:.3f} \nÁREA CÍRCULO = {aC:.3f} \nÁREA TRAPÉZIO = {aT:.3f} \nÁREA QUADRADO = {aQ:.3f} \nÁREA RETÂNGULO = {aR:.3f}');
print();

dias = int(input('Digite a sua idade em dias: '));
anos = int(dias/365);
meses = int((dias - (anos*365))/30);
dias = dias - ((anos * 365) + (meses*30));
print();
print(f'{anos} ano(s), {meses} mes(es) e {dias} dia(s)');
print();

x1 = float(input("X1: "));
y1 = float(input("Y1: "));
x2 = float(input("X2: "));
y2 = float(input("Y2: "));
dist = math.sqrt(pow((x2-x1), 2) + pow((y2-y1), 2));
print();
print(f'DISTÂNCIA = {dist:.4f}');
print();

segundos = int(input('Digite o número de segundos: '));
minutos = int(segundos/60);
segundos -= minutos*60;
horas = int(minutos/60);
minutos -= horas*60;
dias = int(horas/24);
horas -= dias*24
print();
print(f'{dias}  {horas}:{minutos}:{segundos}');
print();

horas = int(input('Digite a quantidade de horas gastas na viagem: '));
vel = int(input('Digite a velocidade média da viagem: '));
dist = horas*vel;
lt = dist/12;
print();
print(f'COMBUSTÍVEL GASTO NA VIAGEM: {lt:.3f}');
print();

dist = int(input('Distância percorrida: '));
lt = float(input('Combustível gasto: '));
lt = dist/lt;
print();
print(f'Consumo médio: {lt:.3f}');
print();

nome = input('Digite o nome do vendedor: ');
sal = float(input('Digite o salário fixo: '));
vendas = float(input('Digite o total de vendas: '));
sal += vendas*0.15;
print();
print(f'VENDEDOR: {nome} \nSALÁRIO RECEBIDO: {sal:.2f}');
print();