from model.aluno import Aluno
from model.professor import Professor
from model.turma import Turma

professor = Professor('Maxwell de Oliveira Chaves',
                        '25/05/1979',
                        'JJJJJJJJJJJJJJJJJJ',
                        'LJJJJJJJJJJJJJJ',
                        '12345678912',
                        '123456123',
                        '11111111111111',
                        'Rua qualquer, número 0',
                        'Superior Completo',
                        'Tecnólogo em Gestão da Tecnologia da Informação')

# print(professor)


turma = Turma('Curso Técnico de Informática para Internet','2023')
turma.professores = [professor.nome]
aluno = Aluno('0001', turma, 'Amable', '18/03/2000', 'Pai', 'Mãe', '12345678912',
              '123456', '666445554',
              'Endereço fictício')
turma.alunos = [aluno.nome]
turma.disciplinas = ['Redes de computadores']

print(turma)
