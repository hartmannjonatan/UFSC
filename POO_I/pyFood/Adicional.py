# CLASSE ADICIONAL - OS ADICIONAIS DISPONÍVEIS EM CADA PRODUTO SÃO REPRESENTADOS COMO OBJETOS DENTRO DO PRÓPRIO PRODUTO

class Adicional():

    def __init__(self, data: dict = None, cod: int = None, nome: str = None, valorAdicional: float = None) -> None:
        if data == None:
            self.setNome(nome)
            self.setValorAdicional(valorAdicional)
            self.setCod(cod)
        else:
            self.setNome(data["nome"])
            self.setValorAdicional(data["valorAdicional"])
            self.setCod(data["cod"])

    def getCod(self) -> int:
        return self.__cod__

    def setCod(self, cod: int) -> None:
        self.__cod__ = cod

    def getNome(self) -> str:
        return self.__nome__

    def setNome(self, nome: str) -> None:
        self.__nome__ = nome

    def getValorAdicional(self) -> float:
        return self.__valorAdicional__

    def setValorAdicional(self, valorAdicional: float) -> None:
        self.__valorAdicional__ = valorAdicional
    
    def persistirAdicional(self) -> dict:
        data = {}
        data["nome"] = self.getNome()
        data["valorAdicional"] = self.getValorAdicional()
        data["cod"] = self.getCod()
        return data