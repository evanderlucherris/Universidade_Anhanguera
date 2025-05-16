# Lista de filmes para classificação
filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

# Mensagem de boas vindas
print("Bem vindo a classificação de filmes!")
print("Você tem 5 filmes para classificar.")
print("Digite '0' a qualquer momento para parar.\n")


# Loop para iterar sobre cada filme na lista
for filme in filmes:

    while True:
        # Solicita a classificação ao usuário
        classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? (ou 0 para parar): ")
        # Verifica se o usuário deseja parar
        if classificacao == '0':
            print(f"Classificação '{filme}' interrompida.")

            break  # Encerra o loop interno com "break"
        # Converte a classificação em número inteiro
        classificacao = int(classificacao)
        # Verifica se a classificação está entro do intervalo válido
        if classificacao < 1 or classificacao > 5:
            print("Por favor, digite uma classificação válida de 1 a 5.")

        else:
            print(f"Você classificou '{filme}' com {classificacao} estrelas.\n")

        break  # Sai do loop interno

print()