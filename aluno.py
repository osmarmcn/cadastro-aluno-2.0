




class Aluno:
    def __init__(self, nome:str, idade:int, curso:str, nota:float) -> None:
        self.matricula = 0
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota
        
    def __repr__(self) -> str:
        return f'{self.nome}, {self.idade}, {self.curso}, {self.nota}'
    
    
if __name__ == '__main__':
    print(Aluno('Osmar', 29, 'Python', 8.8))