# Tupla de convidados
convidados = (f"Alice", "Bob", "Carol", "David", "Eve")

# Lista de confirmações
confirmados = [f"Bob", "David"]

# Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os convidados que ainda não confirmaram
print(f"Convidados que ainda não confirmaram:")

for pessoa in nao_confirmados:

    print(pessoa)

# Enviar lembretes aos não confirmados
print(f"\nEnviando lembretes para os convidados que ainda não confirmaram.")