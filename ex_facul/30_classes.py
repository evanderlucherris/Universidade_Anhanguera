# Define uma classe chamada Pessoa.
class Pessoa:

    # O método __init__ é um construtor, chamado quando um objeto da classe é criado.
    # Ele inicializa os atributos da classe.
    def __init__(self, nome, idade, genero):
        # self é uma convenção em Python que se refere à própria instância da classe.
        # Os parâmetros nome, idade e gênero são passados durante a criação do objeto.
        # Eles são usados para inicializar os atributos da instância.
        self.nome = nome  # Atribui o valor de nome ao atributo nome da instância.
        self.idade = idade  # Atribui o valor de idade ao atributo idade da instância.
        self.genero = genero  # Atribui o valor de gênero ao atributo gênero da instância.

    # O método cumprimentar retorna uma saudação com o nome da pessoa.
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."

    # O método aniversário aumenta a idade da pessoa em 1.
    def aniversario(self):
        self.idade += 1

# Cria uma instância da classe “Pessoa” com os valores “João”, 30 e “Masculino” para nome, idade e gênero, respectivamente.
pessoa1 = Pessoa(f"João", 30, "Masculino")

# Chama o método “cumprimentar” na instância pessoa1 e imprime a saudação.
print(pessoa1.cumprimentar())  # Saída: “Olá, meu nome é João.”

# Acessa o atributo idade da instância pessoa1 e imprime sua idade.
print(f"Idade: {pessoa1.idade}")  # Saída: “Idade: 30”

# Chama o método “aniversário” na instância pessoa1 para aumentar sua idade em 1.
pessoa1.aniversario()

# Acessa o atributo idade atualizado da instância pessoa1 e imprime a nova idade.
print(f"Nova idade: {pessoa1.idade}")  # Saída: “Nova idade: 31”