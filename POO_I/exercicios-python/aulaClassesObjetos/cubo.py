# QUESTÃO 01 - CLASSE CUBO

class Cubo:

    def __init__(self) -> None:
        x = int(input("Digite um número: "))
        self.cubo = x*x*x
    
    def getCubo(self) -> int:
        return self.cubo


