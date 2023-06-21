# CLASSE ENDEREÇO

class Endereco:

    def __init__(self, data: dict = None, cidade: str = None, bairro: str = None, rua: str = None, cep: str = None, num: str = None, complemento: str = None) -> None:
        if data == None:
            self.setCidade(cidade)
            self.setBairro(bairro)
            self.setRua(rua)
            self.setCep(cep)
            self.setNum(num)
            self.setComplemento(complemento)
        else:
            self.setCidade(data["cidade"])
            self.setBairro(data["bairro"])
            self.setCep(data["cep"])
            self.setRua(data["rua"])
            self.setComplemento(data["complemento"])
            self.setNum(data["num"])

    def getCidade(self) -> str:
        return self.__cidade__

    def setCidade(self, cidade: str) -> None:
        self.__cidade__ = cidade

    def getBairro(self) -> str:
        return self.__bairro__

    def setBairro(self, bairro: str) -> None:
        self.__bairro__ = bairro

    def getRua(self) -> str:
        return self.__rua__

    def setRua(self, rua: str) -> None:
        self.__rua__ = rua

    def getCep(self) -> str:
        return self.__cep__

    def setCep(self, cep: str) -> None:
        self.__cep__ = cep

    def getNum(self) -> str:
        return self.__num__

    def setNum(self, num: str) -> None:
        self.__num__ = num

    def getComplemento(self) -> str:
        return self.__complemento__

    def setComplemento(self, complemento: str) -> None:
        self.__complemento__ = complemento

    