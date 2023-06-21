# CLASSE USUÁRIO - (abstrata porque um usuário obrigatoriamente deve ser um Cliente ou uma Loja)

from abc import ABC, abstractmethod

from DataFiles import DataFiles

class Usuario(ABC):

        
    @abstractmethod
    def logar(login: str, senha: str): # Método abstrato para definir o que há de comum entre objetos das classes Loja e Cliente (são usuários e podem logar no sistema)
        pass

    @abstractmethod
    def cadastrar(login: str, senha: str): # Método abstrato para cadastrar um novo usuário (que é implementado nas subclasses)
        pass
    
    @abstractmethod
    def deletar(): # Método abstrato para deletar o cliente/loja e seu respectivo usuário do sistema
        pass

    def persistirNovoUsuario(self, login: str, type: str, senha: str) -> None:
        if DataFiles.getDataJson("usuarios.json", login) == None:
            data = {}
            data["login"] = login
            data["type"] = type
            data["senha"] = senha
            DataFiles.addDataJson("usuarios.json", data, login)
        else:
            raise UserAlreadyRegistered("Usuário já cadastrado no sistema!")

    def deletarUsuario(self, login: str) -> None:
        DataFiles.deleteDataJson("usuarios.json", login)
    
    def validaLogin(self, type: str, login: str, senha: str) -> dict:
        usuario = DataFiles.getDataJson("usuarios.json", login)  # Obtém os dados do usuário com esse login
        if usuario == None:
            raise UserNotFound("Usuário não cadastrado.")
        else:
            if type == usuario["type"]:
                if usuario["login"] == login and usuario["senha"] == senha:
                    dadosUsuario = DataFiles.getDataJson(type+"s.json", login)
                    return dadosUsuario
                else:
                    raise InvalidCredentials("Login e/ou senha inválido(s).")
            else:
                raise UserTypeInvalid(f"Usuário não está cadastrado como {type}.")
    
    def persistirAlteracao(self, login: str, type: str, senha: str) -> None:
        DataFiles.addDataJson("usuarios.json", {"login": login, "senha": senha, "type": type}, login)

# CLASSE PARA ERRO DE USUÁRIO:
class UserNotFound(Exception): # Usuário não cadastrado
    pass

class UserTypeInvalid(Exception): # Quando tenta acessar com o tipo inválido de usuário
    pass

class InvalidCredentials(Exception): # Senha e/ou login incorreto (mas existente no sistema)
    pass

class UserAlreadyRegistered(Exception): # Quando tenta cadastrar um usuário com um login já existente
    pass