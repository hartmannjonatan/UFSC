# CLASSE PRODUTO

from Adicional import Adicional

class Produto:

    def __init__(self, data: dict = None, cod: int = None, nome: str = None, descricao: str = None, valor: float = None, adicionais: list = []) -> None:
        self.__cod__ = None
        self.__nome__ = None
        self.__valor__ = None
        self.__descricao__ = None
        self.__adicionais__ = []
        if data == None:
            self.setCod(cod)
            self.setNome(nome)
            self.setDescricao(descricao)
            self.setValor(valor)
            self.setAdicionais(adicionais)
        else:
            self.setCod(data["cod"])
            self.setNome(data["nome"])
            self.setDescricao(data["descricao"])
            self.setValor(data["valor"])
            if len(data["adicionais"]) >= 1:
                for adicional in data["adicionais"]:
                    self.addAdicional(adicional["nome"], adicional["valorAdicional"], adicional["cod"])
            else:
                self.setAdicionais([])
            


    def getCod(self) -> int:
        return self.__cod__

    def setCod(self, cod: int) -> None:
        self.__cod__ = cod

    def getNome(self) -> str:
        return self.__nome__

    def setNome(self, nome: str) -> None:
        self.__nome__ = nome

    def getDescricao(self) -> str:
        return self.__descricao__

    def setDescricao(self, descricao: str) -> None:
        self.__descricao__ = descricao

    def getValor(self) -> float:
        return self.__valor__

    def setValor(self, valor: float) -> None:
        self.__valor__ = valor

    def getAdicionais(self) -> list:
        return self.__adicionais__

    def setAdicionais(self, adicionais: list) -> None:
        self.__adicionais__ = adicionais
    
    def addAdicional(self, nomeAdicional: str, valorAdicional: float, cod: str = None) -> None:
        if cod == None:
            cod = len(self.getAdicionais())

        adc = Adicional(None, cod, nomeAdicional, valorAdicional)
        self.getAdicionais().insert(cod, adc)
    
    def editAdicional(self, cod: int, adicional: Adicional) -> None:
        self.getAdicionais()[cod] = adicional
    
    def searchAdicional(self, cod: int) -> Adicional:
       return self.getAdicionais()[cod]


    def deleteAdicional(self, codAdicional: int) -> None:
        print(self.getAdicionais())
        print(codAdicional)
        self.__adicionais__.pop(codAdicional)
    
    def persistirProduto(self, listaAdicionaisComprados: list = None) -> dict:
        data = {}
        data["nome"] = self.getNome()
        data["cod"] = self.getCod()
        data["valor"] = self.getValor()
        data["descricao"] = self.getDescricao()
        data["adicionais"] = list()
        if listaAdicionaisComprados == None:
            for adicional in self.getAdicionais():
                data["adicionais"].insert(adicional.getCod(), adicional.persistirAdicional())
        else:
            for adicional in listaAdicionaisComprados:
                data["adicionais"].insert(adicional.getCod(), adicional.persistirAdicional())
        return data