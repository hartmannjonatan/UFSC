# CLASSE CLIENTE

class Cliente():
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf   
    
    def get_nome(self):
        return self.nome
    
    def get_sobrenome(self):
        return self.sobrenome
    
    def get_cpf(self):
        return self.cpf
    
    def set_nome(self,novo_nome):
        self.nome = novo_nome
        
    def set_sobrenome(self,novo_sobrenome):
        self.sobrenome = novo_sobrenome
    