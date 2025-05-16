import sqlite3

# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo, se não existir)
conn = sqlite3.connect("funcionarios.db")

# Passo 2: Criar a tabela de funcionários
cursor = conn.cursor()
cursor.execute('''

    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cargo TEXT,
        salario REAL
    )
''')

# Passo 3: Inserir um novo funcionário na tabela
novo_funcionario = (1, "João", "Analista", 5000.00)
cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)", novo_funcionario)
conn.commit()

# Passo 4: Consultar e exibir funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print("Funcionários Cadastrados:")
for funcionario in funcionarios:
    print(funcionario)

# Passo 5: Atualizar informações de um funcionário
atualizacao = ("João Silva", 5500.00, 1)
cursor.execute("UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?", atualizacao)
conn.commit()

# Passo 6: Deletar um funcionário da tabela
id_funcionario_para_deletar = 1
cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario_para_deletar,))
conn.commit()