Nota_1 = int(input('Insira a primeira nota: '))
Nota_2 = int(input('Insira a segunda nota: '))
Nota_3 = int(input('Insira a terceira nota: '))
Nota_4 = int(input('Insira a quarta nota: '))

#observe que utilizamos a função int(), pois, sem ela, o Python entenderia que as notas seriam String

# Calcula a média das notas
media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4

#condição para a aprovação do aluno.

if media >= 6 :
   situacao = 'Aprovado'
else:
   situacao = 'Reprovado'

#dadas as notas, mostramos a média final e a situação do aluno.

print(f"{media}")
print(f"{situacao}")