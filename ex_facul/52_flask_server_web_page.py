from flask import Flask
from flask_ngrok import run_with_ngrok

# Criando a instância do aplicativo Flask
app = Flask(__name__)

# Habilitando o ngrok
run_with_ngrok(app)

# Definindo a rota principal
@app.route('/')
def index():
    return 'Olá, esta é a rota principal do back-end!'

# Executando o aplicativo
if __name__ == '__main__':
    app.run()
