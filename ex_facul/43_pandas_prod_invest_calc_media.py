import pandas as pd

# Criar um dicionário com nomes e idades
dados = {

    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]

}

# Criar uma série a partir do dicionário
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

# Exibir a série de idades
print("Série de Idades:")
print(serie_idades)

# Calcular a média das idades
media_idades = serie_idades.mean()

print("\nMédia de Idades:", media_idades)