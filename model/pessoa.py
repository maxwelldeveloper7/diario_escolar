"""Classe pessoa"""

class Pessoa:
    """Implementação da classe Pessoa"""
    def __init__(self, 
                nome, 
                nascimento, 
                pai, 
                mae, 
                cpf, 
                idendidade, 
                titulo_eleitor,
                endereco):
        """Método construtor da classe pessoa"""
        self.nome = nome
        self.data_nascimento = nascimento
        self.nome_pai = pai
        self.nome_mae = mae
        self.cpf = cpf
        self.identidade = idendidade
        self.titulo_eleitor = titulo_eleitor
        self.endereco = endereco

if __name__ == '__main__':
    pass
