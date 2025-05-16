import seaborn as sns
import matplotlib.pyplot as plt

# Configurando o estilo
sns.set(style="whitegrid")  # opções: darkgrid, whitegrid, dark, white, ticks

# Carregando o conjunto de dados
df_tips = sns.load_dataset('tips')

# Criando uma figura com 3 subgráficos
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Gráfico de barras padrão
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
ax[0].set_title('Total Bill by Sex')

# Gráfico de barras com a soma dos total_bill
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
ax[1].set_title('Sum of Total Bill by Sex')

# Gráfico de barras com a contagem de registros
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
ax[2].set_title('Count of Total Bill by Sex')

# Exibindo os gráficos
plt.tight_layout()
plt.show()
