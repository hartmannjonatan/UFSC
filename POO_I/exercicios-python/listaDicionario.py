# LISTA DE EXERCÍCIOS: DICIONÁRIO

import datetime

# FUNÇÕES GERAIS (MAIS DE UM EXERCÍCIO)

# QUESTÃO 01
# funções questão 01:
def tabelarProdutos(qtd: int):
    tabelaProdutos = {}
    for i in range(0, qtd):
        key, value = input("Digite o nome e o preço do produto separado por um espaço: ").split(" ")
        tabelaProdutos[key] = float(value.replace(",", "."))
    return tabelaProdutos

def listarProdutosCompra(qtd: int):
    lista = {}
    for i in range(0, qtd):
        key, value = input("Digite o nome e a quantidade do produto separado por um espaço: ").split(" ")
        lista[key] = int(value)
    return lista

# for i in range(0, int(input("Digite o número de casos de teste: "))):
#     tabelaProdutos = tabelarProdutos(int(input("Quantidade de produtos no mercado: ")))
#     produtosComprados = listarProdutosCompra(int(input("Quantidade de produtos a serem comprados: ")))
#     total = 0
#     for produtoComprado, qtd in produtosComprados.items():
#         total += qtd*tabelaProdutos[produtoComprado]
#     print(f'Total: R$ {total:.2f}\n')
#     tabelaProdutos.clear()
#     produtosComprados.clear()
        

# QUESTÃO 02
# funções questão 02:
def tabelarFelizNatal(idiomas: int):
    tabelaFelizNatal = {}
    for i in range(0, idiomas):
        key = input("Idioma: ")
        value = input("Tradução: ")
        tabelaFelizNatal[key] = value
    return tabelaFelizNatal

def listarCriancas(criancas: int):
    lista = {}
    for i in range(0, criancas):
        key = input("Nome: ")
        value = input("Idioma: ")
        lista[key] = value
    return lista

# tabelaFelizNatal = tabelarFelizNatal(int(input("Quantidade de idiomas tabelados: ")))
# criancas = listarCriancas(int(input("Quantidade de crianças: ")))
# for crianca, idioma in criancas.items():
#     print(f'\n{crianca} \n{tabelaFelizNatal[idioma]}\n')

# QUESTÃO 03
# qtd = int(input("Quantidade de alunos: "))
# while qtd != 0:
#     listaAlunosOriginal = {}
#     for i in range(0, qtd):
#         key, value = input("Digite o nome do aluno e sua assinatura separado por um espaço: ").split(" ")
#         listaAlunosOriginal[key] = value

#     assFalsas = 0
#     for i in range(0, int(input("Quantidade de alunos que frequentam a aula: "))):
#         key, value = input("Digite o nome do aluno e sua assinatura separado por um espaço: ").split(" ")
#         if listaAlunosOriginal[key] != value:
#             assFalsas += 1
    
#     print(f'{assFalsas}\n')
#     qtd = int(input("Quantidade de alunos: "))

# QUESTÃO 04
# str = "brasil Feliz Natal!\nalemanha Frohliche Weihnachten!\naustria Frohe Weihnacht!\ncoreia Chuk Sung Tan!\nespanha Feliz Navidad!\ngrecia Kala Christougena!\nestados-unidos Merry Christmas!\ninglaterra Merry Christmas!\naustralia Merry Christmas!\nportugal Feliz Natal!\nsuecia God Jul!\nturquia Mutlu Noellerargentina Feliz Navidad!\nchile Feliz Navidad!\nmexico Feliz Navidad!\nantardida Merry Christmas!\ncanada Merry Christmas!\nirlanda Nollaig Shona Dhuit!\nbelgica Zalig Kerstfeest!\nitalia Buon Natale!\nlibia Buon Natale!\nsiria Milad Mubarak!\nmarrocos Milad Mubarak!\njapao Merii Kurisumasu!"
# str = str.split("\n")
# idiomas = {}
# for el in str:
#     aux = el.split(" ")
#     key = aux[0]
#     value = el.replace(key+" ", "")
#     idiomas[key] = value

# print(f'{idiomas.get(input("Idioma: "), "--- NÃO ENCONTRADO ---")}')

# QUESTÃO 05
# aux = int(input("Digite o número de números na matriz: "))
# while aux != 0:
#     matriz = input("Matriz: ").split(" ")
#     for n in matriz:
#         if matriz.count(n) % 2 != 0:
#             print(n)
#             break
    
#     aux = int(input(f"\nDigite o número de números na matriz: "))

# QUESTÃO 06
# alunos = {}
# for i in range(0, int(input("Digite o número de alunos: "))):
#     key, value = input("").split(" ")
#     alunos[key] = value

# ehd = 0
# epr = 0
# intrusos = 0
# for matr, curso in alunos.items():
#     if str(curso).upper() == "EHD":
#         ehd += 1
#     elif str(curso).upper() == "EPR":
#         epr += 1
#     else:
#         intrusos += 1

# print(f'\nEPR: {epr} \nEHD: {ehd} \nINTRUSOS: {intrusos}\n')

# QUESTÃO 07
# funções da questão 07:
def palavrasHayPoint(qtd: int):
    palavras = {}
    for i in range(0, qtd):
        key, value = input("").split(" ")
        palavras[key] = float(value)
    return palavras

def salarioByDesc(n: int, palavras: dict):
    for i in range(0, n):
        soma = 0
        while True:
            str = input("")
            if str != ".":
                for word in str.split(" "):
                    soma += palavras.get(word, 0)
            else:
                print(f'\nRESULTADO DESCRIÇÃO {i+1}: {soma:.2f}\n')
                break

# m, n = input("").split(" ")
# palavras = palavrasHayPoint(int(m))
# salarioByDesc(int(n), palavras)

# QUESTÃO 08
# função da questão 08:
def cadastrarParticipante(nome: str, p1: str, p2: str, p3: str, listaParticipantes: dict):
    presentes = [p1, p2, p3]
    listaParticipantes[nome] = presentes
    return listaParticipantes

# participantes = {}
# for i in range(0, int(input("Digite o número de participantes: "))):
#     nome, p1, p2, p3 = input("").split(" ")
#     participantes = cadastrarParticipante(nome, p1, p2, p3, participantes)

# for i in range(0, int(input("Quantidade de tentativas de presente: "))):
#     nome, presente = input(" ").split(" ")
#     if presente in list(participantes[nome]):
#         print("Uhul! Seu amigo secreto vai adorar o/")
#     else:
#         print("Tente Novamente!")

# QUESTÃO 09
# função da questão 09:
def verificaCompasso(compass: str, notas: dict):
    soma = 0
    for nota in compass:
        soma += notas[nota]
    return soma == 1

# notas = {"W": 1, "H": 0.5, "Q": 0.25, "E": float(1/8), "S": float(1/16), "T": float(1/32), "X": float(1/64)}

# str = input("")
# while str != "*":
#     compass = str.split("/")
#     corretos = 0
#     for c in compass:
#         if verificaCompasso(c, notas):
#             corretos += 1
#     print(f'\n{corretos}\n')
#     str = input("")

# QUESTÃO 10
# funções da questão 10:
def cadastrarUsuario(nome: str, anoNasc: int, carteira: int):
    usuario= {}
    year = int(datetime.datetime.now().date().strftime("%Y"))
    idade = year - anoNasc
    usuario["nome"] = nome
    usuario["idade"] = idade
    usuario["carteira"] = carteira
    if carteira != 0:
        contrat = int(input("Ano de contratação: "))
        sal = float(input("Salário: "))
        aposentadoria = contrat+35
        usuario["anoContratacao"] = contrat
        usuario["salario"] = sal
        usuario["anoAposentadoria"] = aposentadoria
    print(f"\n-------------------------- USUÁRIO CADASTRADO! --------------------------\n")
    return usuario

def buscaUsuario(nome: str, usuarios: dict):
    verif = usuarios.get(nome, False)
    if verif != False:
        print(f'\nNome: {usuarios[nome]["nome"]} \nIdade: {usuarios[nome]["idade"]} \nCarteira: {usuarios[nome]["carteira"]}')
        if usuarios[nome]["carteira"] != 0:
            print(f'\nAno Contratação: {usuarios[nome]["anoContratacao"]} \nSalário: R$ {usuarios[nome]["salario"]:.2f} \nAno Aposentadoria: {usuarios[nome]["anoAposentadoria"]}')
    else:
        print('USUÁRIO NÃO CADASTRADO')
    print(f'\n------------------------------------------------------------------------\n')

def printUsuarios(usuarios: dict):
    print(f"\n----------------------------- USUÁRIOS -----------------------------\n")
    for usuario in usuarios.values():
        print(f'\n{usuario}')
    print(f'\n------------------------------------------------------------------------\n')

def printMenu():
    print(f"\n----------------------------- MENU -----------------------------\n")
    print(f'[1] - Cadastrar novo usuário')
    print(f'[2] - Buscar usuário')
    print(f'[3] - Imprimir todos os usuários')
    print(f'[0] - Sair')
    esc = int(input(F"\nESCOLHA: "))
    print(f'\n------------------------------------------------------------------------\n')
    return esc

usuarios = {}

esc = printMenu()
while esc != 0:
    if esc == 1:
        print(f"\n----------------------------- CADASTRAR -----------------------------\n")
        nome = input("Nome: ")
        anoNasc = int(input("Ano de nascimento: "))
        carteira = int(input("Carteira de trabalho: "))
        usuarios[nome] = cadastrarUsuario(nome, anoNasc, carteira)
    elif esc == 2:
        print(f"\n----------------------------- BUSCA USUÁRIO -----------------------------\n")
        nome = input("Nome: ")
        buscaUsuario(nome, usuarios)
    elif esc == 3:
        printUsuarios(usuarios)
    else:
        print(f'\n------------------------------------------------------------------------\n')
        print('OPÇÃO INEXISTENTE')
        print(f'\n------------------------------------------------------------------------\n')

    esc = printMenu()
