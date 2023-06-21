# CLASSE VEÍCULO

class Veiculo():

    def __init__(self, nome, marca, cor, litrosTanque) -> None:
        self.nome = nome
        self.marca = marca
        self.cor = cor
        self.litrosTanque = litrosTanque
    
    def print(self):
        print(f"O veículo {self.nome} da {self.marca} e cor {self.cor}, está atualmente com {self.litrosTanque} litro(s) no tanque de combustível.")

    def abastecer(self, litros):
        self.litrosTanque += litros