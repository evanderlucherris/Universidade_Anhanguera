# Importe as bibliotecas necessárias
import numpy as np

# Dados dos participantes
participantes = [

    {
        "nome": "Alice",
        "localizacao": "EUA",
        "afiliacao": "Universidade A",
        "interesses": ["Física", "Astronomia"]
    },
    {
        "nome": "Bob",
        "localizacao": "Brasil",
        "afiliacao": "Instituto B",
        "interesses": ["Biologia", "Astronomia"]
    },
    {
        "nome": "Charlie",
        "localizacao": "Índia",
        "afiliacao": "Instituto C",
        "interesses": ["Química", "Engenharia"]
    }

    # Adicione mais participantes conforme necessário
]

# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante["localizacao"] for participante in participantes)

# Usando um dicionário para categorizar afiliações
afiliacoes = {}

for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

# Usando NumPy para analisar áreas de interesse
areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

# Resultados
print(f"Regiões dos participantes:", regioes)
print(f"Afiliações dos participantes:")

for afiliacao, nomes in afiliacoes.items():
    print(f'{afiliacao}: {', '.join(nomes)}')

print(f"Área de interesse mais popular:", area_mais_popular)