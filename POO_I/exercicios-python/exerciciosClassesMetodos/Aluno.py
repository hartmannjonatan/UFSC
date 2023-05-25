# LISTA CLASSES E MÉTODOS UTILITÁRIOS - CLASSE ALUNO

class Aluno:
    def __init__(self, nome: str, curso: str, tempo: int) -> None:
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempo
    
    def estudar(self, tempo: int):
        self.tempoSemDormir += tempo
    
    def dormir(self, horas: int):
        self.tempoSemDormir -= horas
    
    def getTempoSemDormir(self) -> int:
        return self.tempoSemDormir
    
    def getNome(self) -> str:
        return self.nome