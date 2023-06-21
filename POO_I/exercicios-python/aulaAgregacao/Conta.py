# CLASSE CONTA

from Historico import Historico

class Conta():
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))
        print(f"Depositado R$ {valor:.2f}")

    def retira(self,valor):
        if self.saldo < valor:
            print("Saldo insuficiente! Saque cancelado!")
        else:
            print(f"Sacado R$ {valor:.2f}")
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):
        print(f"Conta: {self.numero} - Saldo: {self.saldo}")
        self.historico.transacoes.append(f"tirou extrato - saldo de {self.saldo}")
        self.historico.imprime()

    def transfere(self, destino, valor):
        if self.saldo > valor:
            self.saldo -= valor
            destino.saldo += valor
            destino.historico.transacoes.append(f"Recebido tranferência de R$ {valor} da conta {self.numero}")
            self.historico.transacoes.append(f"transferencia de {valor} para conta {destino.numero}")
            print(f"Transferido R$ {valor:.2f} para conta {destino.numero}")
        else:
            print("Saldo insuficiente! Transferência cancelada!")