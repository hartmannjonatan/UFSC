# MAIN

# OBS AS LINHAS COMENTADAS SÃO PARA EXEMPLIFICAR A FUNCIONALIDADE DO SISTEMA SEM O USO DA INTERFACE

# from Cliente import Cliente
# from Loja import Loja
# from Produto import Produto
# from Adicional import Adicional
# from Cupom import Cupom
# from Pedido import Pedido
# from Endereco import Endereco
from Interface import Interface
# from DataFiles import DataFiles

# c1 = Cliente("joao123", "12345")
# c1.addCupom(Cupom(None, "SWEETPRICE"))
# c1.persistirCliente()

# pedido = Pedido("restaurante_floripa", c1, Endereco(None, "Florianópolis", "Pantanal", "Servidão João de Assis", "88096-68", "22", "Ap 06"))
# pedido.addProduto(0, 3, [0])
# pedido.calcularSubtotal()
# pedido.calcularTotal(10.0, c1.getCupom(1))
# pedido.emitirPedido()

# l1 = Loja("acaiDaIlha", "acaiBarato", "Açaí da Ilha", Endereco(None, "Florianópolis", "Carvoeira", "R. Rio Branco", "98690-000", "120"), "Sorveterias")
# p1 = Produto(None, None, "Açaí 500ml - Monte o Seu", "Açaí de 500ml, permite até 3 adicionais", 15.00, [])
# p1.addAdicional("Leite em pó", 3.0)
# p1.addAdicional("Banana", 3.0)
# p1.addAdicional("Morango", 4.0)
# p1.addAdicional("Leite condensado", 2.0)
# p1.addAdicional("Oreo", 5.0)
# p1.addAdicional("Nutella", "5.0")

# l1.addProduto(None, p1)
# l1.persistirLoja()

# pedido = Pedido("acaiDaIlha", c1, Endereco(None, "Florianópolis", "Pantanal", "Servidão João de Assis", "88096-68", "22", "Ap 06"))
# pedido.addProduto(0, 1, [1])
# pedido.calcularSubtotal()
# pedido.calcularTotal(7.0, c1.getCupom(0))
# pedido.emitirPedido()

view = Interface()

