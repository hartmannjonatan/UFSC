# LISTA CLASSES E MÉTODOS UTILITÁRIOS - CLASSE LIVRO

class Livro:

    def __init__(self, nome: str, pag: int, autor: str) -> None:
        self.nome = nome
        self.qtdPag = pag
        self.autor = autor
        self.preco = 0
    
    def getPreco(self) -> float:
        return self.preco
    
    def getQtdPag(self) -> int:
        return self.qtdPag
    
    def getNome(self) -> str:
        return self.nome
    
    def getAutor(self) -> str:
        return self.autor
    
    def setPreco(self, preco: float):
        self.preco = preco
    
    def info(self):
        print(f'Nome: {self.getNome()}, Qtd Pág.: {self.getQtdPag()}, Autor: {self.getAutor()}, Preço: R$ {self.getPreco()}')
    