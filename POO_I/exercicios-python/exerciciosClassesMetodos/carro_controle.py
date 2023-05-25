# LISTA CLASSES E MÉTODOS UTILITÁRIOS - CONTROLE CARRO

from Carro import Carro

meuFusca = Carro(15)
meuFusca.addCombustivel(20)
meuFusca.andar(100)
print(f"Combustível do carro instanciado: {meuFusca.getCombustivel():.2f} litros.")