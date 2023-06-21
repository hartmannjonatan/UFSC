# CLASSE CARRO

from Veiculo import Veiculo


class Carro(Veiculo):
    
    def __init__(self, nome, marca, cor, litrosTanque) -> None:
        super().__init__(nome, marca, cor, litrosTanque)
        self.limiteTanque = 50
    
    def print(self):
        print(f"O veículo {self.nome} da {self.marca} e cor {self.cor}, está atualmente com {self.litrosTanque}/{self.limiteTanque} litro(s) no tanque de combustível.")
    
    def abastecer(self, litros):
        if (self.litrosTanque + litros) <= self.limiteTanque:
            super().abastecer(litros)
        else:
            aux = self.limiteTanque - self.litrosTanque
            print(f"Capacidade máxima do tanque alcançada. Foi possível abastecer {aux} litro(s).")
            super().abastecer(aux)