import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro:

    def __init__(self, titulo, autor, ano_publicacao):

        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"

# Criar uma lista de livros
biblioteca = []
anos = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)
    print(f"O livro '{titulo}' foi adicionado à biblioteca.")

# Função para listar todos os livros na biblioteca
def listar_livros():
    print("Livros na biblioteca:")
    for livro in biblioteca:
        print(livro)

# Adicionar alguns livros à biblioteca
adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e Preconceito", "Jane Auten", 1813)
adicionar_livro("1984", "Jorge Orwell", 1949)
adicionar_livro("Cem Anos de Solidão", "Gabriel garcia Marques", 1967)
adicionar_livro("Apanhador no Campo de Centeio", "J.D. Salinger", 1951)

# Listar todos os livros na biblioteca
listar_livros()

# Criar um gráfico de livros por ano
anos = list(set(anos))# Remove duplicatas dos anos
anos.sort()

