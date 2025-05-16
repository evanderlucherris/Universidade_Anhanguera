import sqlite3

# 1. Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
create_table = """

CREATE TABLE IF NOT EXISTS Produtos (

    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER

);

"""

# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. Confirmar as alterações (commit)
conn.commit()

# 6. Fechar a conexão com o banco de dados
conn.close()