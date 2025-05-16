media = 8.5

if(media>=7.0):
    situacao="Aprovado"
elif(media>=5.0):
    situacao="Em Recuperação"
else:
    situacao="Reprovado"

print(f'O estudante está: {situacao}')