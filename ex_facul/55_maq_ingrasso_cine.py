# Bem-vindo à Máquina de Venda Automática de Ingressos de Cinema!

 

# Solicita a idade do cliente

idade = int(input(f"Por favor, digite sua idade: "))

 

# Verifica a idade para sugestão de filmes

if idade < 12:

    print(f"Recomendamos o filme infantil FILME 1.")

elif 12 <= idade < 18:

    print(f"Recomendamos o filme adolescente FILME 2.")

else:

    print(f"Recomendamos o emocionante FILME 3.")

 

# Verifica a disponibilidade de ingressos

quantidade_ingressos = 10  # Suponha que haja 10 ingressos disponíveis

if quantidade_ingressos > 0:

    print(f"Ingressos estão disponíveis. Divirta-se no cinema!")

else:

    print(f"Desculpe, todos os ingressos estão esgotados para hoje.")

