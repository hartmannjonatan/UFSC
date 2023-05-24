# QUESTÃO 02 - CONTROLE FUNCIONÁRIO

from funcionario import Funcionario

f1 = Funcionario(input(f"Digite o nome do funcionário 1: "), float(input(f'Digite o salário do funcionário 1: ')))
f1.calculaAumento()
f1.printFuncionario()

print("\n")

f2 = Funcionario(input(f"Digite o nome do funcionário 2: "), float(input(f'Digite o salário do funcionário 2: ')))
f2.calculaAumento()
f2.printFuncionario()

print("\n")

f3 = Funcionario(input(f"Digite o nome do funcionário 3: "), float(input(f'Digite o salário do funcionário 3: ')))
f3.calculaAumento()
f3.printFuncionario()