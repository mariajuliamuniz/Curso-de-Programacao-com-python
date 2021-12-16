class Aluno:
    aluno_matriculado = True
    def __init__ (self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
    def __str__ (self):
        return f'nome: {self.nome}, matricula: {self.matricula}, curso: {self.curso}'

aluno_1 = Aluno ('Maria Julia', 'Fisica', '314796')

print(aluno_1)
