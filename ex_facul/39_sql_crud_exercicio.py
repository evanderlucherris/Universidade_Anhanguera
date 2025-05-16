import sqlite3

# CREATE (Criação da tabela e inserção de dados de exemplo)
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute('''

    CREATE TABLE IF NOT EXISTS Contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT

    )

''')

dados_exemplo = [

    ('João', 'joao@email.com', '123-456-7890'),
    ('Maria', 'maria@email.com', '987-654-3210'),
    ('Carlos', 'carlos@email.com', '555-555-5555')

]

cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)', dados_exemplo)
conn.commit()

# READ (Leitura e exibição dos contatos)
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print("Contatos:")

for contato in contatos:
    print(contato)

# UPDATE (Atualização do número de telefone do contato com ID 2)
novo_telefone = '999-999-9999'
contato_id = 2
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()

# DELETE (Exclusão do contato com ID 1)
contato_id_para_excluir = 1

cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_para_excluir,))
conn.commit()

# Fechando a conexão
conn.close()