# LISTA CONJUNTOS

todos = {'João', 'Maria', 'Pedro', 'Fernando'}
natacao = {'João', 'Maria'}
futebol = {'Maria', 'Fernando'}
volei = {'João', 'Pedro'}
basquete = {'João',  'Pedro', 'Fernando'}

while True:
    op = input('Deseja matricular um novo aluno? [S/N]: ')
    if op.upper() == "S":
        aluno = input('Nome do aluno: ')
        todos.add(aluno)
        if input('Matricular na natação [S/N]: ').upper() == 'S':
            natacao.add(aluno)
        if input('Matricular no futebol [S/N]: ').upper() == 'S':
            futebol.add(aluno)
        if input('Matricular no volei [S/N]: ').upper() == 'S':
            volei.add(aluno)
        if input('Matricular no basquete [S/N]: ').upper() == 'S':
            basquete.add(aluno)
    else:
        break
        
print(f'{len(natacao)} alunos matriculados em natação: {natacao}')
print(f'{len(futebol)} alunos matriculados em futebol: {futebol}')
print(f'{len(volei)} alunos matriculados em volei: {volei}')
print(f'{len(basquete)} alunos matriculados em basquete: {basquete}')
print(f'Total de alunos: {len(todos)}\n')
print(f'Alunos com direito a desconto de 50%: {natacao.intersection(futebol).union(futebol.intersection(basquete).union(basquete.intersection(volei).union(volei.intersection(natacao))))}')

todos = {'João', 'Pedro', 'Maria', 'Luciana', 'Marta'}
e1 = {'João', 'Pedro', 'Maria'}
e2 = { 'Luciana', 'Marta'}

while True:
    op = input('Deseja cadastrar um novo cliente? [S/N]: ')
    if op.upper() == "S":
        cliente = input('Nome: ')
        todos.add(cliente)
        if input('Cadastrar na empresa A [S/N]: ').upper() == 'S':
            e1.add(cliente)
        if input('Cadastrar na empresa B [S/N]: ').upper() == 'S':
            e2.add(cliente)
    else:
        break

print(f'{len(e1)} clientes cadastrados na empresa A: {e1}')
print(f'{len(e2)} clientes cadastrados na empresa B: {e2}')
inters = e1.intersection(e2)
print(f'{len(inters)} clientes cadastrados em ambas as empresas: {inters}')
print(f'{len(e1.symmetric_difference(e2))} clientes cadastrados em apenas uma das empresas: {e1.symmetric_difference(e2)}')
print(f'{len(todos)} = todos os clientes: {todos}')