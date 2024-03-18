"""
    Classe aluno
"""
from .pessoa import Pessoa
from .turma import Turma

class Aluno(Pessoa):
    """Implementação da classe Aluno"""
    def __init__(self,
                matricula,
                turma: Turma,
                nome,
                nascimento,
                pai,
                mae,
                cpf,
                idendidade,
                titulo_eleitor,
                endereco):        
        """Método construtor da classe Aluno"""
        super().__init__(nome, nascimento, pai, mae, cpf, idendidade, 
                        titulo_eleitor, endereco)
        self.matricula = matricula
        self.turma = turma

    def __str__(self):
        """Retorna dados do Aluno em forma de texto"""
        return 'Matrícula: {}, Nome: {}, Turma: {} '.format(
            self.matricula,
            self.nome,
            self.turma.nome
        )

if __name__ == '__main__':
    pass
