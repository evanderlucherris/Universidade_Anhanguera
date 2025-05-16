#Estratégia 01

lista = [10, 2, 5, 7, 6, 3]
n=len(lista)
soma=0
for i in range(n):
    if(lista[i]%2==0):
        soma=soma+lista[i]
print(f'O somatório dos elementos pares é: {soma}')

#Estratégia 02

lista = [10, 2, 5, 7, 6, 3]

soma =0
for num in lista:
    if(num%2==0):
        soma=soma+num
print(f'O somatório dos elementos pares da lista é: {soma}')