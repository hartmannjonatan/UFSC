# CLASSE CUPOM (desconto)

from DataFiles import DataFiles

class Cupom():

    __cod__ = None
    __desconto__ = None
    __valorMinimo__ = 0.0
    __categoria__ = None

    def __init__(self, data: dict = None, cod: str = None) -> None:
        if data == None:
            if self.validarCupom(cod):
                self.setCod(cod)
        else:
            self.setCod(data["cod"])
            self.setDesconto(data["desconto"])
            self.setValorMinimo(data["valorMinimo"])
            self.setCategoria(data["categoria"])

    def getCod(self) -> str:
        return self.__cod__

    def setCod(self, cod: str) -> None:
        self.__cod__ = cod

    def getDesconto(self) -> float:
        return self.__desconto__

    def setDesconto(self, desconto: float) -> None:
        self.__desconto__ = desconto

    def getCategoria(self) -> str:
        return self.__categoria__

    def setCategoria(self, categoria: str) -> None:
        self.__categoria__ = categoria

    def getValorMinimo(self) -> float:
        return self.__valorMinimo__

    def setValorMinimo(self, valorMinimo: float) -> None:
        self.__valorMinimo__ = valorMinimo
    
    def persistirCupom(self) -> dict:
        data = {}
        data["cod"] = self.getCod()
        data["categoria"] = self.getCategoria()
        data["valorMinimo"] = self.getValorMinimo()
        data["desconto"] = self.getDesconto()
        return data

    def validarCupom(self, cod: str) -> bool:
        
        cupom = DataFiles.getDataJson("cuponsValidos.json", cod)
        if cupom == None:
            raise CupomNotFound("Cupom inválido!")
        else:
            self.setCategoria(cupom["categoria"])
            self.setCod(cupom["cod"])
            self.setDesconto(cupom["desconto"])
            self.setValorMinimo(cupom["valorMinimo"])

# CLASSE PARA ERRO RELACIONADO AO CUPOM:
class CupomNotFound(Exception): # CUPOM INVÁLIDO
    pass

class CupomInvalidForCategory(Exception): # CUPOM INVÁLIDO REFERENTE À CATEGORIA DA LOJA
    pass

class CupomInvalidForPrice(Exception): # CUPOM INVÁLIDO PELO VALOR MÍNIMO DE COMPRA
    pass