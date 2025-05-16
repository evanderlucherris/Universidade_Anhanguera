import pandas as pd
import matplotlib.pyplot as plt

# Dados
dados = {
    'Produto': ['A', 'B', 'C'],
    'qtde_vendida': [34, 70, 33]
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Gráfico de barras
df.plot(x='Produto', y='qtde_vendida', kind='bar')
plt.title('Quantidade Vendida por Produto')
plt.ylabel('Quantidade Vendida')
plt.show()  # Exibe o gráfico de barras

# Gráfico de pizza
df.plot(x='Produto', y='qtde_vendida', kind='pie', legend=False)
plt.title('Participação de Cada Produto')
plt.ylabel('')  # Remove o rótulo do eixo y
plt.show()  # Exibe o gráfico de pizza

# Gráfico de linhas
df.plot(x='Produto', y='qtde_vendida', kind='line', marker='o')
plt.title('Quantidade Vendida ao Longo do Tempo')
plt.ylabel('Quantidade Vendida')
plt.show()  # Exibe o gráfico de linhas