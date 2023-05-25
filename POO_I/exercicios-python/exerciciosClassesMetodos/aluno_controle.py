# LISTA CLASSES E MÉTODOS UTILITÁRIOS - CONTROLADOR ALUNO

from Aluno import Aluno

a1 = Aluno("João", "CCO", 0)
a1.estudar(8)
a1.dormir(2)
a1.estudar(4)
print(f"Tempo sem dormir de {a1.getNome()} é {a1.getTempoSemDormir()} hora(s).")