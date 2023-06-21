# CLASSE PEDIDO

from Loja import Loja
from Cliente import Cliente
from Endereco import Endereco
from Cupom import *
from Produto import Produto
from datetime import datetime
from DataFiles import DataFiles

class Pedido():


    def __init__(self, loginLoja: str, cliente: Cliente, enderecoEntrega: Endereco) -> None: # FAZER
        self.__cod__ = None
        self.__loja__ = None
        self.__cliente__ = None
        self.__datetime__ = None
        self.__produtosComprados__ = {}
        self.__enderecoEntrega__ = None
        self.__taxaEntrega__ = 0.0
        self.__subtotal__ = 0.0
        self.__cupom__ = None
        self.__total__ = 0.0
        loja = DataFiles.getDataJson("lojas.json", loginLoja)
        loja = Loja(loja["login"], loja["senha"])
        self.setLoja(loja)
        self.setCliente(cliente)
        self.setDatetime(datetime.now())
        self.setEnderecoEntrega(enderecoEntrega)
        self.setCod(loja.getLogin()+self.getDatetime().strftime('%d%m%y')+cliente.getCpf()[-3]+self.getDatetime().strftime('%H%M%S'))

    def getCod(self) -> str:
        return self.__cod__

    def setCod(self, cod: str) -> None:
        self.__cod__ = cod

    def getLoja(self) -> Loja:
        return self.__loja__

    def setLoja(self, loja: Loja) -> None:
        self.__loja__ = loja

    def getCliente(self) -> Cliente:
        return self.__cliente__

    def setCliente(self, cliente: Cliente) -> None:
        self.__cliente__ = cliente

    def getDatetime(self) -> datetime:
        return self.__datetime__

    def setDatetime(self, datetime: datetime) -> None:
        self.__datetime__ = datetime

    def getProdutosComprados(self) -> dict:
        return self.__produtosComprados__

    def setProdutosComprados(self, produtosComprados: dict) -> None:
        self.__produtosComprados__ = produtosComprados
    
    def addProduto(self, codProduto: int, quantidade: int, adicionaisLista: list = []) -> None:
        produto = self.getLoja().searchProduto(codProduto)
        produtoComprado = {}
        produtoComprado["quantidade"] = quantidade
        produtoComprado["produto"] = produto
        adicionais = []
        total = produto.getValor()
        for adicional in adicionaisLista:
            adc = produto.searchAdicional(adicional)
            adicionais.append(adc)
            total += adc.getValorAdicional()
        produtoComprado["adicionais"] = adicionais
        produtoComprado["totalProduto"] = total
        self.getProdutosComprados()[len(self.getProdutosComprados())] = produtoComprado

    def deleteProduto(self, codProduto: int) -> None:
        self.getProdutosComprados().pop(codProduto)

    def getEnderecoEntrega(self) -> Endereco:
        return self.__enderecoEntrega__

    def setEnderecoEntrega(self, enderecoEntrega: Endereco) -> None:
        self.__enderecoEntrega__ = enderecoEntrega

    def getTaxaEntrega(self) -> float:
        return self.__taxaEntrega__

    def setTaxaEntrega(self, taxaEntrega: float) -> None:
        self.__taxaEntrega__ = taxaEntrega

    def getSubtotal(self) -> float:
        return self.__subtotal__

    def setSubtotal(self, subtotal: float) -> None:
        self.__subtotal__ = subtotal
    
    def calcularSubtotal(self) -> None:
        subtotal = 0.0
        for produtoComprado in self.getProdutosComprados().values():
            subtotal += produtoComprado["quantidade"]*produtoComprado["totalProduto"]
        self.setSubtotal(subtotal)

    def getCupom(self) -> Cupom:
        return self.__cupom__

    def setCupom(self, cupom: Cupom = None) -> None:
        self.__cupom__ = cupom
        if cupom != None:
            if cupom.getCategoria() == self.getLoja().getCategoria() or cupom.getCategoria() == "QUALQUER_CATEGORIA":
                if cupom.getValorMinimo() <= self.getSubtotal():
                    desconto = cupom.getDesconto()
                    total = self.getTotal()
                    self.setTotal(total - total*desconto)
                else:
                    raise CupomInvalidForPrice("O subtotal do pedido é menor do que o valor mínimo para o cupom ser utilizado!")
            else:
                raise CupomInvalidForCategory("A categoria do cupom não é compatível com a categoria desta loja!")

    def getTotal(self) -> float:
        return self.__total__

    def setTotal(self, total: float) -> None:
        self.__total__ = total
    
    def calcularTotal(self, taxaEntrega: float, cupom: Cupom = None) -> None: # FAZER
        self.calcularSubtotal() # Subtotal = todos os produtos, Total = (subtotal - desconto*subtotal) + taxa de entrega
        self.setTotal(self.getSubtotal())
        self.setCupom(cupom) # Desconta o cupom
        self.setTaxaEntrega(taxaEntrega)
        total = self.getTotal() + self.getTaxaEntrega()
        self.setTotal(total)


    def emitirPedido(self) -> None:
        self.persistirPedido()
        self.getCliente().addPedido(None, self)
        self.getLoja().addVenda(None, self)

    def persistirPedido(self, retornarData: bool = False) -> dict or None:
        data = {}
        data["cod"] = self.getCod()
        loja = {}
        loja["nome"] = self.getLoja().getNome()
        loja["categoria"] = self.getLoja().getCategoria()
        loja["login"] = self.getLoja().getLogin()
        data["loja"] = loja
        cliente = {}
        cliente["cpf"] = self.getCliente().getCpf()
        cliente["nome"] = self.getCliente().getNome()
        cliente["login"] = self.getCliente().getLogin()
        data["cliente"] = cliente
        endereco = {}
        endereco["cidade"] = self.getEnderecoEntrega().getCidade()
        endereco["bairro"] = self.getEnderecoEntrega().getBairro()
        endereco["rua"] = self.getEnderecoEntrega().getRua()
        endereco["cep"] = self.getEnderecoEntrega().getCep()
        endereco["num"] = self.getEnderecoEntrega().getNum()
        endereco["complemento"] = self.getEnderecoEntrega().getComplemento()
        data["enderecoEntrega"] = endereco
        produtosComprados = {}
        for key, produtoComprado in self.getProdutosComprados().items():
            produto = {}
            produto["quantidade"] = produtoComprado["quantidade"]
            produto["produto"] = produtoComprado["produto"].persistirProduto(produtoComprado["adicionais"])
            produto["produto"]["totalProduto"] = produtoComprado["totalProduto"]
            produtosComprados[key] = produto
        data["produtosComprados"] = produtosComprados
        data["datetime"] = self.getDatetime().strftime("%d/%m/%Y %H:%M:%S")
        data["taxaEntrega"] = self.getTaxaEntrega()
        data["total"] = self.getTotal()
        data["subtotal"] = self.getSubtotal()
        cupom = {}
        if self.getCupom() != None:
            cupom["cod"] = self.getCupom().getCod()
            cupom["desconto"] = self.getCupom().getDesconto()
            cupom["categoria"] = self.getCupom().getCategoria()
            cupom["valorMinimo"] = self.getCupom().getValorMinimo()
        data["cupom"] = cupom

        if retornarData:
            return data
        else:
            DataFiles.addDataJson("pedidos.json", data, self.getCod())
            return data

    def deletar(self) -> None:
        DataFiles.deleteDataJson("pedidos.json", self.getCod())