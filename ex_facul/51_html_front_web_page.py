# Criando uma página HTML usando Python

html_code = """
<!DOCTYPE html>
<html>
<head>
  <title>Exemplo de Front-end com Python</title>
</head>
<body>
  <h1>Olá, mundo!</h1>
  <p>Esta é uma página web criada usando Python no Google Colab.</p>
</body>
</html>
"""

# Exibindo a página HTML
from IPython.display import HTML

HTML(html_code)
