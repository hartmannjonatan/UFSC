# LISTA CLASSES E MÉTODOS UTILITÁRIOS - CLASSE CARRO

class Carro:
    def __init__(self, consumo: float) -> None:
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, dist: float) -> None:
        self.combustivel -= dist/self.consumo
    
    def getCombustivel(self) -> float:
        return self.combustivel
    
    def addCombustivel(self, combustivel: float) -> None:
        self.combustivel += combustivel
        