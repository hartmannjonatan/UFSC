# CLASSE CLIENTE

from Cupom import Cupom
from Usuario import Usuario
from DataFiles import DataFiles

class Cliente(Usuario):

    def __init__(self, login: str, senha: str, nome: str = None, cpf: str = None) -> None: # Quando o construtor recebe como parâmetro apenas login e senha ele loga o usuário, caso contrário cadastra um novo
        self.__login__ = None
        self.__senha__ = None
        self.__nome__ = None
        self.__cpf__ = None
        self.__cupons__ = []
        self.__historicoPedidos__ = {}
        if nome == None and cpf == None:
            self.logar(login, senha)
        else:
            self.setNome(nome)
            self.setCpf(cpf)
            self.cadastrar(login, senha)
    
    def getSenha(self) -> str:
        return self.__senha__

    def setSenha(self, senha: str) -> None:
        self.__senha__ = senha
        

    def getLogin(self) -> str:
        return self.__login__

    def setLogin(self, login: str) -> None:
        self.__login__ = login
        

    def getNome(self) -> str:
        return self.__nome__

    def setNome(self, nome: str) -> None:
        self.__nome__ = nome
        

    def getCpf(self) -> str:
        return self.__cpf__

    def setCpf(self, cpf: str) -> None:
        self.__cpf__ = cpf
        

    def getCupons(self) -> list:
        return self.__cupons__
    
    def getCupom(self, indexCupom: int) -> Cupom:
        return self.getCupons()[indexCupom]
    
    def useCupom(self, cupom: Cupom) -> None:
        for index, c in enumerate(self.getCupons()):
            if cupom.getCod() == c.getCod():
                self.getCupons().pop(index)
                break

    def setCupons(self, cupons: list) -> None:
        self.__cupons__ = cupons
    
    def addCupom(self, cupom: Cupom) -> None:
        self.getCupons().append(cupom)
        

    def getHistoricoPedidos(self) -> dict:
        return self.__historicoPedidos__

    def setHistoricoPedidos(self, historicoPedidos: dict) -> None:
        self.__historicoPedidos__ = historicoPedidos
    
    def addPedido(self, data: dict = None, pedido = None) -> None:
        if data == None:
            self.getHistoricoPedidos()[pedido.getCod()] = pedido.persistirPedido(True)
            if pedido.getCupom() != None:
                self.useCupom(pedido.getCupom())
            self.persistirCliente()
        else:
            self.getHistoricoPedidos()[data["cod"]] = data

    def logar(self, login: str, senha: str) -> None:
        data = super().validaLogin("cliente", login, senha)
        self.setLogin(data["login"])
        self.setSenha(data["senha"])
        self.setNome(data["nome"])
        self.setCpf(data["cpf"])
        for pedido in data["historicoPedidos"].values():
            self.addPedido(pedido)
        cupons = data["cupons"]
        for cupom in cupons:
            self.addCupom(Cupom(cupom))

    def cadastrar(self, login: str, senha: str) -> None:
        super().persistirNovoUsuario(login, "cliente", senha)
        self.setLogin(login)
        self.setSenha(senha)
        self.persistirCliente()
    
    def deletar(self) -> None:
        super().deletarUsuario(self.getLogin())
        DataFiles.deleteDataJson("clientes.json", self.getLogin())
    
    def persistirCliente(self) -> None:
        data = {}
        data["login"] = self.getLogin()
        data["senha"] = self.getSenha()
        data["nome"] = self.getNome()
        data["cpf"] = self.getCpf()
        cupons = []
        for cupom in self.getCupons():
            cupons.append(cupom.persistirCupom())
        data["cupons"] = cupons
        data["historicoPedidos"] = self.getHistoricoPedidos()
        DataFiles.addDataJson("clientes.json", data, self.getLogin())
        super().persistirAlteracao(self.getLogin(), "cliente", self.getSenha())