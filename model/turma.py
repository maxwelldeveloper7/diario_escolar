"""Classe Turma"""

class Turma:
    """Implementação da classe Turma"""
    def __init__(self, nome, ano):
        """Método construtor"""
        self.nome = nome
        self.ano = ano
        self.disciplinas = []
        self.professores = []
        self.alunos = []

    def __str__(self):
        """Retorna as inforações em forma de texto"""
        
        return "Turma: {}\nAno: {}\nDisciplnas: {}\nProfessores: {}\
            \nAlunos: {}".format(
            self.nome,
            self.ano,
            self.disciplinas,
            self.professores,
            self.alunos          
        )

if __name__ == '__main__':
    pass
