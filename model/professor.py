"""Classe Professor"""
from .pessoa import Pessoa

class Professor(Pessoa):
    """Implementação da classe Pessoa"""
    def __init__(self, nome, nascimento, pai, mae, cpf, idendidade, 
                titulo_eleitor, endereco, escolaridade, titulacao):
        """Método construtor"""
        super().__init__(nome, nascimento, pai, mae, cpf, idendidade,
                        titulo_eleitor, endereco)
        self.escolaridade = escolaridade
        self.titulacao = titulacao
        self.turmas = []

    def __str__(self):
        return f"Nome: {self.nome} - Turmas: {self.turmas}"