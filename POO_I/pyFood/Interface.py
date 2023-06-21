# CLASSE INTERFACE

from Adicional import Adicional
from Cliente import Cliente
from Cupom import Cupom
from Endereco import Endereco
from Loja import Loja
from DataFiles import DataFiles
import eel

from Pedido import Pedido
from Produto import Produto

class Interface:

    user = None
    type = None

    def __init__(self) -> None:
        eel.init("web")
        eel.start("login.html", mode='fullscreen')
    
    @eel.expose
    def logar(type: str = None, login: str = None, senha: str = None):
        if Interface.user == None:
            Interface.type = type
            if type == "cliente":
                try:
                    user = Cliente(login, senha)
                    Interface.user = user
                    data = DataFiles.ObjToJson(user.getLogin(), type)
                    return data
                except Exception as e:
                    return {"error": str(e)}
            else:
                try:
                    user = Loja(login, senha)
                    Interface.user = user
                    data = DataFiles.ObjToJson(user.getLogin(), type)
                    return data
                except Exception as e:
                    return {"error": str(e)}
        else:
            data = DataFiles.ObjToJson(Interface.user.getLogin(), Interface.type)
            return data
    
    @eel.expose
    def logout():
        Interface.user = None
        Interface.type = None
    
    @eel.expose
    def editUser(value):
        if Interface.type == "cliente":
            Interface.user.setNome(value["nome"])
            Interface.user.setCpf(value["cpf"])
            Interface.user.setLogin(value["login"])
            Interface.user.setSenha(value["senha"])
            Interface.user.persistirCliente()
        else:
            Interface.user.setNome(value["nome"])
            Interface.user.setCategoria(value["categoria"])
            Interface.user.setEndereco(Endereco(value["endereco"]))
            Interface.user.setSenha(value["senha"])
            Interface.user.persistirLoja()
    
    @eel.expose
    def deleteUser():
        Interface.user.deletar()
        Interface.user = None
        return {"delete": "success"}

    @eel.expose
    def validarCupom(cod):
        try:
            cupom = Cupom(None, cod)
            Interface.user.addCupom(cupom)
            Interface.user.persistirCliente()
            return cupom.persistirCupom()
        except Exception as e:
            return {"error": str(e)}
    
    @eel.expose
    def getAllLojas():
        data = DataFiles.getDataJson("lojas.json")
        lojas = {}
        for key, loginLoja in enumerate(data):
            loja = data[loginLoja]
            aux = {}
            aux["login"] = loja["login"]
            aux["nome"] = loja["nome"]
            aux["endereco"] = loja["endereco"]
            aux["categoria"]= loja["categoria"]
            aux["produtos"] = loja["produtos"]
            aux["quantidadeVendas"] = loja["quantidadeVendas"]
            lojas[key] = aux
        return lojas

    @eel.expose
    def novoPedido(data: dict, calcularTotal: 0 = None):
        pedido = Pedido(data["loja"]["login"], Interface.user, Endereco(data["enderecoEntrega"]))
        for produto in data["produtosComprados"]:
            listaAdicionais = []
            for adicional in produto["adicionais"]:
                listaAdicionais.append(int(adicional["cod"]))
            pedido.addProduto(int(produto["produto"]["cod"]), int(produto["quantidade"]), listaAdicionais)
        try:
            pedido.calcularSubtotal()
            cupom = None
            if data["cupom"] != None and data["cupom"] != "null":
                cupom = int(data["cupom"])
                pedido.calcularTotal(10.0, Interface.user.getCupom(cupom))
            else:
                pedido.calcularTotal(10.0)
            if calcularTotal == 0:
                pedido.emitirPedido()
            else:
                return {"total": pedido.getTotal()}
        except Exception as e:
            return {"error": str(e)}
    
    @eel.expose
    def validarNovoLogin(login):
        users = DataFiles.getDataJson("usuarios.json")
        for user in users.keys():
            if login == user:
                return False
        
        return login
    
    @eel.expose
    def cadastrarCliente(data):
        cliente = Cliente(data["login"], data["senha"], data["nome"], data["cpf"])
        return {"cadastro": "success"}

    @eel.expose
    def cadastrarLoja(data):
        print(data)
        loja = Loja(data["login"], data["senha"], data["nome"], Endereco(data["endereco"]), data["categoria"])
        return {"cadastro": "success"}

    @eel.expose
    def getAllCategories():
        data = DataFiles.getDataJson("lojas.json")
        categorias = set()
        for key, loginLoja in enumerate(data):
            loja = data[loginLoja]
            categorias.add(loja["categoria"])
        return list(categorias)

    @eel.expose
    def newProduto(produto):
        produto = Produto(None, None, produto["nome"], produto["descricao"], produto["valor"], [])
        Interface.user.addProduto(None, produto)
        Interface.user.persistirLoja()
        return produto.persistirProduto()
    
    @eel.expose
    def editProduto(produto):
        novoProduto = Produto(produto)
        Interface.user.editProduto(produto["cod"], novoProduto)
        Interface.user.persistirLoja()
        return {"editProduto": "success"}

    @eel.expose
    def addAdicional(codProduto, adicional):
        Interface.user.getProdutos()[codProduto].addAdicional(adicional["nome"], adicional["valor"])
        Interface.user.persistirLoja()
        return {"newAdicional": "success"}
    
    @eel.expose
    def editAdicional(codProduto: int, adicional):
        novoAdicional = Adicional(adicional)
        Interface.user.searchProduto(codProduto).editAdicional(adicional["cod"], novoAdicional)
        Interface.user.persistirLoja()
        return {"editProduto": "success"}
    
    @eel.expose
    def deleteAdicional(codProduto, codAdicional):
        Interface.user.searchProduto(codProduto).deleteAdicional(codAdicional)
        Interface.user.persistirLoja()
        return {"delete": "success"}
    
    @eel.expose
    def deleteProduto(codProduto):
        Interface.user.deleteProduto(codProduto)
        Interface.user.persistirLoja()
        return {"delete": "success"}