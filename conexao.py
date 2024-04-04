import pymysql.cursors
from aluno import Aluno

class Conexao:

    def __init__(self) -> None:
        self.conexao = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'escola',
            cursorclass = pymysql.cursors.DictCursor
        )

    def insert(self, aluno:Aluno):
        
        with self.conexao.cursor() as cursor:
            try:
                sql = 'INSERT INTO alunos (nome, idade, curso, nota) VALUES '\
                        "(%s, %s, %s, %s)"
                cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.nota))
                self.conexao.commit()

            except Exception as error:
                print(f'erro ao inserir! {error}')

    def update(self, aluno:Aluno):
        with self.conexao.cursor() as cursor:
            sql = 'UPDATE alunos SET nome = %s, idade = %s,curso = %s,' \
                "nota = %s WHERE matricula = %s"
            
            cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.nota, aluno.matricula))
            self.conexao.commit()

    def delete(self, matricula:int):
        with self.conexao.cursor() as cursor:
            sql = 'DELETE FROM alunos WHERE matricula = %s'
            cursor.execute(sql, matricula)
            self.conexao.commit()

    def listar(self):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM alunos"
            cursor.execute(sql)
            alunos = cursor.fetchall()
            return alunos
        



if __name__ == '__main__':
    a = Conexao()
    alu = Aluno('Pedro', 21, 'Java', 6.7)
    alu.matricula = 1
    a.insert(alu)
    alu.nome = 'Jose'
    a.update(alu)
    print(a.listar())
    