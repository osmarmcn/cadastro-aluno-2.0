# from aluno import Aluno
# from conexao import Conexao
# import pymysql.cursors

# class Alunodata:
#     def insert(self, aluno:Aluno):
        
#         with self.conexao.cursor() as cursor:
#             try:
#                 sql = 'INSERT INTO alunos (nome, idade, curso, nota) VALUES '\
#                         "(%s, %s, %s, %s)"
#                 cursor.execute(sql(aluno.nome, aluno.idade, aluno.curso, aluno.nota))
#                 self.conexao.commit()

#             except Exception as error:
#                 print(f'erro ao inserir! {error}')


# if __name__ == '__main__':
#     Alunodata()
