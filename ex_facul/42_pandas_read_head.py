import pandas as pd

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)

df_bancos.head()