import pandas as pd

# Criando um dicionário com pares chave-valor
data = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

# Criando uma Series a partir do dicionário
series2 = pd.Series(data)

print(series2)