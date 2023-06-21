# CLASSE LOJA

from Endereco import Endereco
from Produto import Produto
from Usuario import Usuario
from DataFiles import DataFiles

class Loja(Usuario):


    def __init__(self, login: str, senha: str, nome: str = None, endereco: Endereco = None, categoria: str = None) -> None:
        self.__login__ = None
        self.__senha__ = None
        self.__nome__ = None
        self.__endereco__ = None
        self.__categoria__ = None
        self.__produtos__ = []
        self.__quantidadeVendas__ = 0
        self.__totalVendas__ = 0.0
        self.__historicoVendas__ = {}
        if nome == None and endereco == None and categoria == None:
            self.logar(login, senha)
        else:
            self.setNome(nome)
            self.setEndereco(endereco)
            self.setCategoria(categoria)
            self.cadastrar(login, senha)

    def getLogin(self) -> str:
        return self.__login__

    def setLogin(self, login: str) -> None:
        self.__login__ = login

    def getSenha(self) -> str:
        return self.__senha__

    def setSenha(self, senha: str) -> None:
        self.__senha__ = senha

    def getNome(self) -> str:
        return self.__nome__

    def setNome(self, nome: str) -> None:
        self.__nome__ = nome

    def getEndereco(self) -> Endereco:
        return self.__endereco__

    def setEndereco(self, endereco: Endereco) -> None:
        self.__endereco__ = endereco

    def getCategoria(self) -> str:
        return self.__categoria__

    def setCategoria(self, categoria: str) -> None:
        self.__categoria__ = categoria

    def getProdutos(self) -> list:
        return self.__produtos__

    def setProdutos(self, produtos: list) -> None:
        self.__produtos__ = produtos

    def getQuantidadeVendas(self) -> int:
        return self.__quantidadeVendas__

    def setQuantidadeVendas(self, quantidadeVendas: int) -> None:
        self.__quantidadeVendas__ = quantidadeVendas

    def getTotalVendas(self) -> float:
        return self.__totalVendas__

    def setTotalVendas(self, totalVendas: float) -> None:
        self.__totalVendas__ = totalVendas

    def getHistoricoVendas(self) -> dict:
        return self.__historicoVendas__

    def setHistoricoVendas(self, historicoVendas: dict) -> None:
        self.__historicoVendas__ = historicoVendas
    
    def addProduto(self, data: dict = None, produto: Produto = None) -> None:
        if data == None:
            produto.setCod(len(self.getProdutos()))
        else:
            if data["cod"] == None:
                data["cod"] = len(self.getProdutos())
            produto = Produto(data)

        self.getProdutos().insert(produto.getCod(), produto)

    def editProduto(self, cod: int, produto: Produto) -> None:
        self.getProdutos()[cod] = produto
            
    
    def deleteProduto(self, codProduto: int) -> None:
        self.__produtos__.pop(codProduto)

    def searchProduto(self, codProduto: int) -> Produto:
        return self.__produtos__[codProduto]
    
    def addVenda(self, data: dict = None, venda = None) -> None:
        
        if data == None:
            self.setQuantidadeVendas(self.getQuantidadeVendas() + 1)
            self.getHistoricoVendas()[venda.getCod()] = venda.persistirPedido(True)
            self.setTotalVendas(self.getTotalVendas() + venda.getTotal())
            self.persistirLoja()
        else:
            self.getHistoricoVendas()[data["cod"]] = data
            
    
    def searchVenda(self, codPedido: str):
        return self.__historicoVendas__[codPedido]

    def logar(self, login: str, senha: str) -> None:
        data = super().validaLogin("loja", login, senha)
        self.setLogin(data["login"])
        self.setSenha(data["senha"])
        self.setNome(data["nome"])
        self.setCategoria(data["categoria"])
        self.setQuantidadeVendas(data["quantidadeVendas"])
        self.setTotalVendas(data["totalVendas"])
        self.setEndereco(Endereco(dict(data["endereco"])))
        for produto in data["produtos"]:
            self.addProduto(produto)
        for venda in data["historicoVendas"].values():
            self.addVenda(venda)

    def persistirLoja(self):
        data = {}
        data["login"] = self.getLogin()
        data["senha"] = self.getSenha()
        data["nome"] = self.getNome()
        endereco = {}
        endereco["cidade"] = self.getEndereco().getCidade()
        endereco["bairro"] = self.getEndereco().getBairro()
        endereco["rua"] = self.getEndereco().getRua()
        endereco["cep"] = self.getEndereco().getCep()
        endereco["num"] = self.getEndereco().getNum()
        endereco["complemento"] = self.getEndereco().getComplemento()
        data["endereco"] = endereco
        data["categoria"] = self.getCategoria()
        produtos = []
        for produto in self.getProdutos():
            produtos.insert(produto.getCod(), produto.persistirProduto())
        data["produtos"] = produtos
        data["quantidadeVendas"] = self.getQuantidadeVendas()
        data["totalVendas"] = self.getTotalVendas()
        data["historicoVendas"] = self.getHistoricoVendas()

        DataFiles.addDataJson("lojas.json", data, self.getLogin())
        super().persistirAlteracao(self.getLogin(), "loja", self.getSenha())
    
    def cadastrar(self, login: str, senha: str):
        super().persistirNovoUsuario(login, "loja", senha)
        self.setLogin(login)
        self.setSenha(senha)
        self.persistirLoja()

    def deletar(self):
        super().deletarUsuario(self.getLogin())
        DataFiles.deleteDataJson("lojas.json", self.getLogin())
        
