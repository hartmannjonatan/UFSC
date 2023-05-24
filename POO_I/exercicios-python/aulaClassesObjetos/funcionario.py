# QUESTÃO 02 - CLASSE FUNCIONÁRIO

class Funcionario:

    def __init__(self, nome: str, salAtual: float) -> None:
        self.nome = nome
        self.salAtual = salAtual

    def calculaAumento(self):
        if self.salAtual <= 2000:
            self.salReajuste = self.salAtual*1.15
        elif self.salAtual > 2000 and self.salAtual <= 3000:
            self.salReajuste = self.salAtual*1.1
        else:
            self.salReajuste = self.salAtual*1.05
        
    def printFuncionario(self):
        print(f'Funcionário {self.nome} \nSalário Atual: R$ {self.salAtual:.2f} \nSalário com reajuste: R$ {self.salReajuste:.2f}')